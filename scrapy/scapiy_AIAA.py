from bs4 import BeautifulSoup
import csv
import requests
import random
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent
import re
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
	title = resultsoup.find('div', {"class":"hlFld-Title"})
	name_find = resultsoup.find('div',{'class','artAuthors'})
	abstract_a = resultsoup.find('div', {"class":"abstractSection"})
	time = resultsoup.find('div',{'class','datePadding'})

	

	if title is None :
		title = 'null'
		row.append(title)
	else:
		row.append(title.get_text())
	if name_find is None:
		author_list = 'null'
		row.append(author_list)
	else:
		authors = name_find.find_all('span',{'class','NLM_string-name'})
		if len(authors)==0:
			author_list = 'null'
			row.append(author_list)
		else:
			author_list = authors[0].get_text()
			for j in range(1,len(authors)):
				author_list=author_list+';'+authors[j].get_text()
		row.append(author_list)
	if time is None:
		timeresult= 'null'
		row.append(timeresult)
	else:
		time_list= time.get_text().split(' ')
		timeresult= time_list[-3]+time_list[-2]+time_list[-1]
		row.append(timeresult)
	if abstract_a is None :
		abstract_a = 'null'
		row.append(abstract_a)
	else:
		row.append(abstract_a.find('p').get_text())
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
	
	baseurl="https://arc.aiaa.org"
	ua = UserAgent()
	ua = ua.random
	HEADERS = {"User-Agent":ua}
	out=open("/home/cbq/Desktop/scapiy/AIAA.csv",'a',newline='')
	csv_write=csv.writer(out,dialect='excel')
	Article_sort = []
	# (57)48
	
	for j in range(1,3):	
		firstone = 'https://arc.aiaa.org/toc/aiaaj/57/{0}'.format(j)
		proxies2 = get_ip()
		Volume_req = requests.get(firstone,headers=HEADERS,proxies=proxies2)
		Volumesoup = BeautifulSoup(Volume_req.content, features='lxml')
		article = Volumesoup.find_all('a', {'class', 'ref nowrap'})
		for i in article:
			if re.search('abs',i.get('href')) is None:
				pass					
			else:
				Article_sort.append(i.get('href'))

					
	num= 5
	proxies3 = get_ip()
	for i in range(5,len(Article_sort)):
		num= num+1
		print(num)
		url_art = baseurl+Article_sort[i]
		print(url_art)
		if num % 3 == 0:
			proxies3 = get_ip()
		else:
			pass
		get(url_art,HEADERS,csv_write,out,proxies3)
	print('over')
	out.close()
