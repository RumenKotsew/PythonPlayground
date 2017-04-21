import requests
from bs4 import BeautifulSoup, SoupStrainer

response = requests.get('http://www.start.bg')
hrefs = []
soup = BeautifulSoup(response.content, "lxml", parse_only=SoupStrainer('a'))
for link in soup.find_all('a'):
    with open('servers.txt', 'w') as f:
        try:
            result_link = link.get('href')
            if result_link == '#top' or result_link is None or result_link == 'javascript':
                continue
            else:
                print(requests.head(result_link).headers['server'])
                f.append(requests.head(result_link).headers['server'] + "\n")
                f.close()
        except Exception as e:
            pass
