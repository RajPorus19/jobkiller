from bs4 import BeautifulSoup as bs4
import requests
import json
from lxml import html
from pprint import pprint
import re

url = 'https://fr.indeed.com/jobs?q=informatique&l=Île-de-France&start=10/'
r = requests.get(url)
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')

scripts = soup.find_all("script")
flag = "jobmap = {};"

for script in scripts:
    if flag in str(script):
        parse = str(script).split("\n")

for i in parse:
    if i.startswith("jobmap["):
        pass
        #print(i,'\n')

def main():
    soup = get_indeed_jobs_html("informatique","Île-de-France",10)
    jobmapsFromHtml = parse_indeed_jobs_list(soup)
    print(jobmapsFromHtml)
    indeedJson = all_indeed_jobs_json(jobmapsFromHtml)
    print(indeedJson)

def get_indeed_jobs_html(jobtitle,location,pageNum):
    url = 'https://fr.indeed.com/jobs?q={}&l={}&start={}/'.format(jobtitle,location,pageNum)
    r = requests.get(url)
    html_bytes = r.text
    indeedSoup = bs4(html_bytes, 'lxml')
    return indeedSoup 

def parse_indeed_jobs_list(indeedSoup):
    scriptTags = indeedSoup.find_all("script")
    flag = "jobmap = {};"
    jobmapsFromHtml = []
    parsedScript = ""
    print(scriptTags)

    for script in scriptTags:
        if flag in script:
            parsedScript = script.split("\n")
    for line in parsedScript:
        if line.startswith("jobmap["):
            jobmapsFromHtml.append(line)

    return jobmapsFromHtml

def jobmap_to_json(jobmapString):

    indexOfEqualSign = jobmapString.find("=")
    indexOfSemiColon = jobmapString.rfind(";")
    
    jobmapJsonStr = jobmapString[indexOfEqualSign + 1 : indexOfSemiColon]

    jobmapJson = json.loads(jobmapJsonStr)
    return jobmapJson

def all_indeed_jobs_json(jobmapsFromHtml):
    indeedJson = json.loads("{}")
    for jobmapStr in jobmapsFromHtml:
        jobmapJson = jobmap_to_json(jobmapStr)
        if jobmapJson not in indeedJson["jobs"]:
            indeedJson["jobs"] += jobmapJson
    return indeedJson

main()
