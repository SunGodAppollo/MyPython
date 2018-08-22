# -*- coding: utf-8 -*-
import urllib2
import sys
import u
import re

from  Save import  SaveFile
from  Save import  SaveExcel


class OnePage():
    """docstring for ."""
    def __init__(self):
        self.url="https://www.banggood.com/search/"
        pass
    #通过连接获取html页面
    def getHtmlByUrl(self,number):
        url=self.url+str(number)+".html?sbc=1"
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #获得系统编码格式
        type = sys.getfilesystemencoding()
        rqs=urllib2.urlopen(url)
        html=rqs.read().decode('utf-8').encode(type)
        return html
    #通过页面获取网页的跳转连接
    def getNewUrlByHtml(self,html):
        result=re.match('<li(.*?)</li>',html)
        print(result.group())
        return 1
    #获得真实的连接地址
    def getResUrl(self,number):
        htnl=self.getHtmlByUrl(number)
        return self.getNewUrlByHtml(html)
    #通过html获得bin对象
    def getBinByHtml(self,html):
        pass
    #通过bin对象存储到excel
    def saveBinToExcel(self,bin):
        pass
if __name__ == '__main__':
        #url="https://www.banggood.com/search/957372.html?sbc=1"
        page=OnePage()
        html=page.getHtmlByUrl(957372)
        #f = open('test.txt', 'w')
        #f.write(html)
        #f.close()
        url=page.getNewUrlByHtml(html)
        print(url)
