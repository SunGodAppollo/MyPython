# -*- coding: utf-8 -*-
import urllib2
import sys
import u

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
        pass
    #通过html获得bin对象
    def getBinByHtml(self,html):
        pass
    #通过bin对象存储到excel
    def saveBinToExcel(self,bin):
        pass
if __name__ == '__main__':
        #url="https://www.banggood.com/search/957372.html?sbc=1"
        page=OnePage()
        print(page.getHtmlByUrl(957372))
