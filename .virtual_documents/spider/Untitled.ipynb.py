from  requests_html import HTMLSession,UserAgent


session=HTMLSession()
ua=UserAgent().random
url='https://movie.douban.com/tag/#/?sort=U&range=0,10get_ipython().run_line_magic("27%27&tags=%E7%94%B5%E5%BD%B1,2020'", "")


r=session.get(url,headers={'User-Agent':ua})
r.encoding='gb2312'  


print(r.text)




