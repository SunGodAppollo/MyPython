# -*- coding: utf-8 -*-
import urllib2
import sys
import u



c=u.n()

reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()

rqs=urllib2.urlopen('http://www.baidu.com')


html=rqs.read().decode('utf-8').encode(type)


print type
print rqs.code
print rqs.info()
print html
