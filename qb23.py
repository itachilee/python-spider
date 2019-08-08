import sys
import requests
from bs4 import BeautifulSoup
import time
class downloader(object):
    def __init__(self):
        self.server = 'https://www.x23qb.com'
        self.target = 'https://www.x23qb.com/book/7901/'
        self.names = [] # 存放章节名
        self.urls = [] # 存放链接
        self.nums = 0 # 存放章节数
        self.title = ''
    def getDownloadurl(self):
        # target = 'https://www.x23qb.com/book/2385/'
        # server = 'https://www.x23qb.com'
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html,'lxml')
        # 获取初级ul
        chapterList = div_bf.find_all('ul',class_='chaw_c')
        self.title = div_bf.find_all("div",class_ = 'd_title')[0].h1.text
        # 再次解析获取超链接
        newSoup = BeautifulSoup(str(chapterList),'lxml')
        newList = newSoup.find_all('a')
        self.nums = len(newList)
        for a in newList:
           # print(a.string,server+a.get('href'))
            self.names.append(a.string)
            self.urls.append(self.server+a.get('href'))
        # time.sleep(0.8)
    def getContent(self,target):
        # target = 'https://www.x23qb.com/book/2385/3335717.html'
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html, 'lxml')
        TextContent = div_bf.find_all(id='TextContent')
        texts = TextContent[0].text.replace('chap_tp();', '')
        texts = texts.replace('chap_bg();','')
        texts = texts.replace('theme();','')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.getDownloadurl()
    print('start downloading...')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '%s.txt'%(dl.title), dl.getContent(dl.urls[i]))
        time.sleep(1)
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('downloaded')
