import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.worldometers.info/coronavirus/#countries'

rq = requests.get(url)
country_dict = {}
content = rq.content
soup = bs(content, 'html.parser')
all_anchors_countries = soup.find_all('a', {"class": "mt_a"})
for country in all_anchors_countries:
    country_dict[country.text] = country['href']
