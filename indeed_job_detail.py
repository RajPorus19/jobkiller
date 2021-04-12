from bs4 import BeautifulSoup as bs4
import requests
import json
from lxml import html
from pprint import pprint
import indeed_job_list
import unicodedata


url = indeed_job_list.main()
url = "https://fr.indeed.com/voir-emploi?q=R&D+Vision&t=D%C3%A9veloppeurs(ses)+informatique&jk=3fc9219d69b065f4"
r = requests.get(url)
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')


def fetchIndeedJobDetailJson(url):
    r = requests.get(url)
    html_bytes = r.text
    soup = bs4(html_bytes, 'lxml')
    jsonTemplate = '''
    {
        "jobDesc":"",
        "advantages":"",
        "workHours":"",
        "extraRewards":"",
        "cursusRequirements":"",
        "remoteWork":"",
        "safetyMeasures":""
    }
    '''
    jobJson = json.loads(jsonTemplate)

    if jobFromIndeed(soup):
        jobJson["jobDesc"] = fillJobDescWithAllTags(soup)

    return jobJson


def jobFromIndeed(soup):
    spanTag = "<span>Postuler</span>"
    if spanTag in str(soup): 
        return True
    return False

def getJobInfoList(soup):
    textList = []
    jobDescDiv = soup.find("div", {"id":"jobDescriptionText"})
    children = jobDescDiv.findChildren(recursive=True)
    for child in children:
        childText = unicodedata.normalize("NFKD",child.text)
        if childText not in textList:
            textList.append(childText)
    return textList

def fillJobDescWithAllTags(soup):
    jobDescDiv = soup.find("div", {"id":"jobDescriptionText"})
    return unicodedata.normalize("NFKD",jobDescDiv.text)

print(fetchIndeedJobDetailJson(url))
