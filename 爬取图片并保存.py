# coding=utf-8
'''
文件说明：
'''
import urllib.request
import os
#网址

#img_url="http://manhua1032-61-174-50-98.cdndm5.com/42/41845/604582/1_8491.jpg?cid=604582&key=717109a5fbda7de4fa6761be00ea0096"
img_url="http://manhua1031-61-174-50-98.cdndm5.com/38/37511/503087/2_9358.jpg?cid=503087&key=717109a5fbda7de4fa6761be00ea0096"
#保存路径
path='3.png'
#伪造浏览器的头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36',
           'Referer':'http://www.1kkk.com/ch1-503087/'}

#请求
req = urllib.request.Request(url=img_url,headers=headers)

print(req.get_full_url())
print(req.get_method())
print(req.get_header('User-Agent', 'no'))
print(req.headers)

#爬取结果
response = urllib.request.urlopen(req)
#得到字节码
img_data = response.read()

with open(path,'wb') as f:  
    f.write(img_data)  
    f.close()  
    print(path+' 文件保存成功')
    



