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
        print(i,'\n')

def get_indeed_jobs_html(jobtitle,location,pageNum);
    url = 'https://fr.indeed.com/jobs?q={}&l={}&start={}/'.format(jobtitle,location,pageNum)
    r = requests.get(url)
    html_bytes = r.text
    indeedSoup = bs4(html_bytes, 'lxml')
    return indeedSoup 

def parse_indeed_jobs_list(indeedSoup):
    scriptTags = indeedSoup.find_all("script")
    flag = "jobmap = {};"
    jobmapsFromHtml = []

    for script in scriptTags:
        if flag in script:
            parsedScript = script.split("\n")
    for line in parsedScript:
        if line.startswith("jobmap["):
            jobmapsFromHtml.append(line)

    return jobmapsFromHtml
