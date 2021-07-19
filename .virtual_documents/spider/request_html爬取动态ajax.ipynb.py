from  requests_html import HTMLSession,UserAgent
import os


def get_header():
    location = os.getcwd() + '/fake_useragent.json'
    ua = UserAgent(path=location)
    return ua.random



session=HTMLSession()
ua = get_header()
url='https://movie.douban.com/tag/#/?sort=U&range=0,10get_ipython().run_line_magic("27%27&tags=%E7%94%B5%E5%BD%B1,2020'", "")



r=session.get(url,headers={'User-Agent':ua})
r.encoding='utf-8'


if r.status_code==200:
    r.html.render()
    print(r.text)



