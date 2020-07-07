from lxml import etree
import requests
# url='http://www.96369.net/indices/77'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url='http://value500.com/BDI.asp'
count=requests.get(url,headers=headers)
count.encoding = "utf-8"
print(count.encoding)  #查看网页返回的字符集类型
print(count.apparent_encoding) #自动判断字符集类型
# tree=etree.HTML(count.text,etree.HTMLParser())
# 获取列名
tree=etree.HTML(count.text,etree.HTMLParser())
col=tree.xpath('//table[@border="1"]//strong/text()')
# res=res.xpath('./text()')
print(col)
# 获取数据
res=tree.xpath('//table[@border="1"]')[1]
res=res.xpath('tr/td/text()')
zhushu=[]
sees=[]
j=0
# c=3
for i in res:
    sees.append(i)
    j=j+1
    if j==2:
        zhushu.append(sees)
        sees=[]
        j=0
import pandas as pd
zhushu=pd.DataFrame(zhushu,columns=col)
# 输出到文件
zhushu.to_excel('../月份BDI.xlsx')