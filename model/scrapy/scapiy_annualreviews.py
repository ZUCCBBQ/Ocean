from bs4 import BeautifulSoup
from urllib.request import urlopen

import csv
import requests
import random
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent

def get_ip():
    ip_list = proxytool().get(num=1)
    ip_touple = ip_list[0]
    ip_head = ip_touple[0]
    ip_last = ip_touple[1]
    proxy_info = {'host': ip_head, 'port': ip_last}
    return proxy_info




def get(str,HEADERS,csv_write,out,proxy_info):
	row = []
	result_req = requests.get(str, headers=HEADERS,proxies=proxy_info)
	resultsoup = BeautifulSoup(result_req.text, features='lxml')
	title = resultsoup.find('article')  
	name = resultsoup.find('p', {"class":"name"})
	abstract_a = resultsoup.find('div', {"class":"abstractSection abstractInFull"})
	time = resultsoup.select('#pb-page-content > div > div:nth-child(1) > div > div > div > div > div.journal-code-fluid > div > div > div > div > div:nth-child(2) > div > div > div > div > section.ar-content-left-col > article > div.article-header > div > p')
	if title is None:
		title = 'null'
		row.append(title)
	else:
		row.append(title.find('h1').get_text())
	if name is None:
		name = 'null'
		row.append(name)
	else:
		row.append(name.get_text())
	if len(time)==0:
		time =  'null'
	else:
		a = time[0].get_text().split('\n')
		row.append(a[1])
	if abstract_a is None:
		abstract_b='null'
		row.append(abstract_b)
	else:
		abstract_b=abstract_a.find('p')
		row.append(abstract_b.get_text())
	print(row)
	csv_write.writerow(row)
	out.flush()




# url获取


if __name__ == '__main__':
	
	baseurl="https://www.annualreviews.org"
	ua = UserAgent()
	ua = ua.random
	HEADERS = {"User-Agent":ua}
	out=open("/home/cbq/Desktop/scapiy/aaa.csv",'a',newline='')
	csv_write=csv.writer(out,dialect='excel')
	Article_sort = []
	# 29
	for i in range(50,29,-1):
		proxies2 = get_ip()
		print(proxies2)
		Volume_req = requests.get('https://www.annualreviews.org/toc/fluid/{0}/1'.format(i), headers=HEADERS,proxies=proxies2)
		Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
		article = Volumesoup.find('form', {"name":"frmAbs"})
		article_1 = article.find_all('a',{'class':'btn icon-html'})
		for j in article_1:
			Article_sort.append(j.get('href'))

	num= 363
	for i in range(363,len(Article_sort)):
		num= num+1
		print(num)
		print(baseurl+Article_sort[i])
		inurl = baseurl+Article_sort[i]
		proxies3 = get_ip()
		get(inurl,HEADERS,csv_write,out,proxies3)
	print('over')
	out.close()
