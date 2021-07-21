from  requests_html import HTMLSession,UserAgent
import os


def get_header():
    location = os.getcwd() + '/fake_useragent.json'
    ua = UserAgent(path=location)
    return ua.random


session=HTMLSession()
ua = get_header()
url='http://news.youth.cn/jsxw/index.htm'


r=session.get(url,headers={'User-Agent':ua})
r.encoding='GB2312' 


if r.status_code == 200:
    print(r.html.html)



