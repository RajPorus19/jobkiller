from jobscraper.indeed.indeed_job_detail import IndeedJobDetail
from bs4 import BeautifulSoup as bs4
import requests
import json

class IndeedJobList:
    def __init__(self,jobtitle,location,jobNum):
        self.indeedQueryUrl = "https://fr.indeed.com/voir-emploi"
        self.jobtitle = jobtitle.replace(" ","+")
        self.location = location.replace(" ","+")
        self.jobNum = jobNum
        self.jobList = []
        self.pageNum = 0

    def get_jobs(self):
        self.scrape_all_pages()
        return self.jobList

    def scrape_all_pages(self):
        while len(self.jobList) < self.jobNum:
            soup = self.get_indeed_jobs_html()
            jobmapsFromHtml = self.parse_indeed_jobs_list(soup)
            self.populate_jobList_with_json(jobmapsFromHtml)
            self.pageNum += 1

    def populate_jobList_with_json(self,jobmapsFromHtml):
        for jobmapStr in jobmapsFromHtml: 
            jobmapJson = self.jobmap_to_json(jobmapStr)
            if jobmapJson not in self.jobList and len(self.jobList) < self.jobNum:
                self.jobList.append(jobmapJson)

    def getIndeedJobDetailFromJson(self,jobmapJson):
        id = "indeed" + jobmapJson["jk"]
        company = jobmapJson["cmp"]
        jobtitle = jobmapJson["title"]
        link = self.jobmap_json_to_link(jobmapJson)
        return IndeedJobDetail(id,link,company,jobtitle)

    def get_indeed_jobs_html(self):
        url = 'https://fr.indeed.com/jobs?q={}&l={}&start={}/'.format(self.jobtitle,self.location,self.pageNum)
        r = requests.get(url)
        html_bytes = r.text
        indeedSoup = bs4(html_bytes, 'lxml')
        return indeedSoup 

    def parse_indeed_jobs_list(self,indeedSoup):
        scriptTags = indeedSoup.find_all("script")
        flag = "jobmap = {};"
        jobmapsFromHtml = []
        parsedScript = ""

        for script in scriptTags:
            if flag in str(script):
                parsedScript = str(script).split("\n")
        for line in parsedScript:
            if line.startswith("jobmap["):
                jobmapsFromHtml.append(line)

        return jobmapsFromHtml

    def jobmap_to_json(self,jobmapString):

        indexOfEqualSign = jobmapString.find("=")
        indexOfSemiColon = jobmapString.rfind(";")

        jobmapJsonStr = jobmapString[indexOfEqualSign + 2 : indexOfSemiColon]
        jobmapJsonStr = self.double_quote_json_fields(jobmapJsonStr)

        jobmapJson = json.loads(jobmapJsonStr)
        return jobmapJson

    def double_quote_json_fields(self,jsonStr):
        jsonStr = str(jsonStr)
        jsonStr = jsonStr.replace("jk", '"jk"')
        fields = [
                "efccid",
                "srcid",
                "cmpid",
                "num",
                "srcname",
                "cmp",
                "cmpesc",
                "cmplnk",
                "loc",
                "country",
                "zip",
                "city",
                "title",
                "locid",
                "rd"]

        for field in fields:
            jsonStr = jsonStr.replace(","+field+":", ',"'+field+'":')
        return jsonStr.replace("'",'"')


    def jobmap_json_to_link(self,jobmapJson):
        id = jobmapJson["jk"]
        company = jobmapJson["cmp"]
        jobtitle = jobmapJson["title"]
        link = self.indeedQueryUrl + "?q={}&t={}&jk={}".format(company,jobtitle,id)
        link = link.replace(" ","+")
        return link

