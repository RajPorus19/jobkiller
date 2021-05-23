from bs4 import BeautifulSoup as bs4
import requests
import json
from jobscraper.models.job import Job
import unicodedata



class IndeedJobDetail:
    def __init__(self,id,url,company,jobtitle):
        self.id = id
        self.url = url
        self.company = company
        self.jobtitle = jobtitle
        r = requests.get(self.url)
        html_bytes = r.text
        self.soup = bs4(html_bytes, 'lxml')

    def get_job_object(self):
        job_object = self._turnIndeedJobIntoJobOject()
        return job_object

    def _turnIndeedJobIntoJobOject(self):
        jobmapJson = self._fetchIndeedJobDetailJson()
        jobDesc = jobmapJson["jobDesc"]
        datePublished = "unkown"
        status = "not applied"
        recruiterEmail = "unkown"
        job = Job(self.id ,self.jobtitle, self.company, jobDesc, datePublished, status, self.url, recruiterEmail)
        return job

    def _isJobFromIndeed(self):
        spanTag = "<span>Postuler</span>"
        if spanTag in str(self.soup): 
            return True
        return False

    def _fetchIndeedJobDetailJson(self):
        jsonTemplate = '''
        {
            "jobDesc":"",
            "advantages":"",
            "workHours":"",
            "extraRewards":"",
            "cursusRequirements":"",
            "remoteWork":"",
            "safetyMeasures":"",
            "salary":"",
            "workplace":"",
            "contractType":""
        }
        '''
        jobJson = json.loads(jsonTemplate)

        if self._isJobFromIndeed():
            jobJson = self._fillJsonWithCorrectTags(jobJson)
        else:
            jobJson["jobDesc"] = self._fillJobDescWithAllTags()
        return jobJson


    def _fillJobDescWithAllTags(self):
        allTags = self._getJobInfoList()
        return "\n".join(allTags)

    def _getJobInfoList(self):
        textList = []
        jobDescDiv = self.soup.find("div", {"id":"jobDescriptionText"})
        children = jobDescDiv.findChildren(recursive=True)
        for child in children:
            childText = unicodedata.normalize("NFKD",child.text)
            if childText not in textList:
                textList.append(childText)
        return textList

    def _fillJsonWithCorrectTags(self,jobDetailJson):
        pTagsFrenchAndItsField = {
                "Avantages":"advantages",
                "Horaires":"workHours",
                "Rémunération":"extraRewards",
                "Formation":"cursusRequirements",
                "Télétravail":"remoteWork",
                "Précautions":"safetyMeasures",
                "Salaire":"salary",
                "Lieu de travail":"workplace",
                "Type d'emploi":"contractType"
        }
        jobInfoList = self._getJobInfoList()
        currentField = "jobDesc"
        for info in jobInfoList:
            for pTag, field in pTagsFrenchAndItsField.items():
                info = unicodedata.normalize("NFKD",info)
                pTag = unicodedata.normalize("NFKD",pTag)
                if info.startswith(pTag):
                    currentField = field
                    break

            jobDetailJson[currentField] += info + "\n"

        return jobDetailJson

