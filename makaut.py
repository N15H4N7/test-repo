import requests
from bs4 import BeautifulSoup

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

success = []
failure = []
scrapers_report = []
news_articles = []
name = 'Makaut'

try:
    base_url = "https://makautwb.ac.in/"
    url = "https://makautwb.ac.in/page.php?id=340"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url,verify=False)


    soup = BeautifulSoup(res.text, "html.parser")

    results = soup.find("div", class_="col-md-9").find_all("a")
    for result in results:
        headline = result.text.strip()
        link = result.get("href").strip()
        if 'https' not in link:
            link = base_url + link
            news_articles.append(('Makaut', headline, link))
        else:
            news_articles.append(('Makaut', headline, link))
    success.append('Makaut')
except Exception as e:
    failure.append(('Makaut', e))
    pass
print(news_articles)

#HTTPSConnectionPool(host='makautwb.ac.in', port=443): Max retries exceeded with url: /page.php?id=340 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)')))