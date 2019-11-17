import time
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    base = 'https://en.wikipedia.org'
    randomWikiGenerator = 'https://en.wikipedia.org/wiki/Special:Random'
    lastTargetWiki = 'https://en.wikipedia.org/wiki/Philosophy'

    linksList = []

    try:
        randomWikiResponse = requests.get(randomWikiGenerator)
        firstBaseUrl = randomWikiResponse.url
        url = firstBaseUrl
    except:
        print('Error while opening Base URL.')
        exit()
    else:
        while url != lastTargetWiki and len(linksList) <= 25 and (url not in linksList):
            linksList.append(url)
            urlContent = BeautifulSoup((requests.get(url)).content, 'html.parser')
            time.sleep(1)
            div_body = urlContent.find('div', {'id': 'mw-content-text'})
            url = div_body.find('a').get('href')
            url = base + url
        print('Maximum number of links found.')
        for link in linksList:
            print(link)
