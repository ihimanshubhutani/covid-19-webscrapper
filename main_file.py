import requests
from bs4 import BeautifulSoup as bs
from countries_name import country_dict


def fetch_covid_details(country_name_path):
    url = f"https://www.worldometers.info/coronavirus/{country_name_path}"

    r = requests.get(url)
    content = r.content
    soup = bs(content, 'html.parser')

    maincounter = soup.find_all('div', {"class": 'maincounter-number'})
    data = []
    for i in maincounter:
        data.append(i.span.text)
    return data
