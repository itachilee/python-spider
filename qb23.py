import requests
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    target = 'https://www.x23qb.com/lightnovel/'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

    req = requests.get(url=target)
    req.encoding="gbk"
    soup =BeautifulSoup(req.text,'lxml')
    # req.encoding='utf-8'
    chapter = soup.find_all('div',class_= 'list')
    recombook = BeautifulSoup(str(chapter),'lxml')
    # e = recombook.dt
    recombook_soup = recombook.find_all('dl')
    print(recombook_soup)