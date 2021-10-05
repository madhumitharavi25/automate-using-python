import requests as r
import bs4 as bs
res = r.get("https://mail.google.com/mail/u/0/?tab=km#inbox")# get data from webpage
res.status_code # 200 -everything ok
#len(res.text) #print the length of the text
#res.raise_for_status()#check status of webpage
file = open("romeo.txt",'wb')
for chunk  in res.iter_content(100000):  # res.iter_content will return chunk
    soup = bs.BeautifulSoup(res.text,'html.parser')
elems = soup.select("html.aAX body.aAU div div.nH div.nH div.nH.w-asV.aiw div.nH.oy8Mbf.qp header#gb.gb_pa.gb_Va.gb_Le.gb_Kd div.gb_Fd.gb_Wd.gb_Md div.gb_Ed.gb_Pd.gb_Ie.gb_xe.gb_De div.gb_ze")
print(elems)
