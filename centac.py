import requests
from bs4 import BeautifulSoup

success = []
failure = []
scrapers_report = []
news_articles = []
name = 'CENTAC'

try:
    url = 'https://www.centacpuducherry.in/'
    base_url = url
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)
    #print(content.status_code)
    soup = BeautifulSoup(content.text,'html.parser')
    notifications = soup.find_all(class_='content text-danger font-weight-bold text-justify')
    for notification in notifications:
        a_tag = notification.find('a')
        headline = a_tag.text.strip()
        link = a_tag['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass