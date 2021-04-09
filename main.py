from bs4 import BeautifulSoup as bs4
import requests
import json
from lxml import html
from pprint import pprint

import re



url = 'https://fr.indeed.com/jobs?q=informatique&l=Île-de-France&start=10/'
#r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"})
r = requests.get(url)
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')


pattern = re.compile(r"swc_market_lists\s+=\s+(\{.*?\})")
script = soup.find("script", text=pattern)

pprint(soup)


