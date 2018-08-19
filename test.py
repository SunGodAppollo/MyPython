# -*- coding: utf-8 -*-
import urllib2
import sys
import u



url="https://www.banggood.com/search/957372.html?sbc=1"

reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()

rqs=urllib2.urlopen(url)


html=rqs.read().decode('utf-8').encode(type)


#print type
#print rqs.code
#print rqs.info()
print html
