import requests
from bs4 import BeautifulSoup

#打开页面
r = requests.get(https://new.baidu.com/)
#获取所有的HTML代码
html_doc = r.text
#解析代码
soup = BeautifulSoup(html_doc, 'html.parser)
#定位HTML页面的标题，获取内容
print(soup.title.text)
