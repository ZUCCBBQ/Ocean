from bs4 import BeautifulSoup
import csv
import requests
import random
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent
import re
import time

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
	title = resultsoup.find('header', {"class":"publicationContentTitle"})

	name_find = resultsoup.find_all('span',{"class":"contrib-author"})
	abstract_a = resultsoup.find('div', {"class":"abstractSection abstractInFull"})
	time = resultsoup.find('div',{"class":"publicationContentEpubDate dates"})
	
	
	if title is None :
		title = 'null'
		row.append(title)
	else:
		title_a = title.find('h3')
		row.append(title_a.get_text())

	if name_find is None:
		author_list = 'null'
		row.append(author_list)
	else:
		author_list = ''
		for i in name_find:
			name = i.find_all('a')
			for j in name:
				if j.get_text() is None:
					pass
				else:
					author_list = author_list+' '+j.get_text()
		row.append(author_list)
	if time is None:
		timeresult = 'null'
		row.append(timeresult)
	else:
		row.append(time.get_text())
	if abstract_a is None :
		abstract_b = 'null'
		row.append(abstract_b)
	else:
		abstract_b = abstract_a.find('div')
		row.append(abstract_b.get_text())
	print(row)
	csv_write.writerow(row)
	out.flush()

# def if_have_next(Volumeurl):
# 	proxies2 = get_random_ip(ip_list)
# 	Volume_req = requests.get(Volumeurl[-1], headers=HEADERS,proxies=proxies2)
# 	Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
# 	next = Volumesoup.find('a',{'class':'next'})
# 	return next


if __name__ == '__main__':
	
	baseurl="https://aip.scitation.org"
	ua = UserAgent()
	ua = ua.random
	HEADERS = {"User-Agent":ua}
	out=open("/home/cbq/Desktop/scapiy/applied_physics.csv",'a',newline='')
	csv_write=csv.writer(out,dialect='excel')
	Article_sort = []
	#108,(125)

	# 24
	count = 0
	proxies2 = get_ip()
	for i in range (120,119,-1):
		for j in range(1,24):
			count= count+1
			if count % 5 == 0:
				proxies2 = get_ip()
			else:
				pass
			print(proxies2)
			firstone = 'https://aip.scitation.org/toc/jap/{0}/{1}'.format(i,j)
			Volume_req = requests.get(firstone,headers=HEADERS,proxies=proxies2)
			Volumesoup = BeautifulSoup(Volume_req.content, features='lxml')
			article = Volumesoup.find_all('a', {'class', 'ref nowrap'})
			for t in article:
				Article_sort.append(t.get('href'))
			time.sleep(0.5)

	num= 0
	proxies3 = get_ip()
	for i in range(0,len(Article_sort)):
		num= num+1
		print(num)
		url_art = baseurl+Article_sort[i]
		print(url_art)
		if num % 3 == 0:
			proxies3 = get_ip()
		else:
			pass
		get(url_art,HEADERS,csv_write,out,proxies3)
		time.sleep(0.5)
	print('over')
	out.close()
