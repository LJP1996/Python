import requests
import re
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/world/')
res.encoding = "utf-8"
pat = re.compile(r'[a-zA-z]+://[^\s]*')
bat = re.compile(r'<[^>]+>',re.S)
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.blk122'):
    for new in news.select('a'):
          print(pat.findall(str(new)),bat.sub('',str(new)))
    
