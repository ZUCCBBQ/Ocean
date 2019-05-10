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


def get(str,csv_write,out,proxy_info):
	row = []

	result_req = requests.get(str, headers=HEADERS,proxies=proxy_info)
	resultsoup = BeautifulSoup(result_req.text, features='lxml')

	title = resultsoup.find('span', {"class":"title-text"})
	abstract_a = resultsoup.find('div', {"class":"abstract author"})
	name1 = resultsoup.find_all('span', {"class":"text given-name"})
	name2 = resultsoup.find_all('span', {"class":"text surname"})
	time = resultsoup.find('div',{'class':'text-xs'})

	if len(name1)==0:
		name = 'null'
	else:
		name  = name1[0].get_text()+name2[0].get_text()
		for i in range(1,len(name1)):
			temp_name = name1[i].get_text()+name2[i].get_text() 
			name = name + ' '+ temp_name
	if title is None:
		title = 'null'
		row.append(title)
	else:
		row.append(title.get_text())
	row.append(name)
	if abstract_a is None:
		abstract_b='null'
		row.append(abstract_b)
	else:
		abstract_b=abstract_a.find('p')
		row.append(abstract_b.get_text())
	if time is None:
		time_in = 'null'
		row.append(time_in)
	else:
		time_in = time.get_text().split(',')
		row.append(time_in[1])
	csv_write.writerow(row)
	out.flush()




# url获取


if __name__ == '__main__':
	
	baseurl="https://www.sciencedirect.com/"
	ua = UserAgent()
	ua = ua.random
	HEADERS = {"User-Agent":ua}
	out=open("/home/cbq/Desktop/scapiy/fluids_and_structures.csv",'a',newline='')
	csv_write=csv.writer(out,dialect='excel')
	Article_sort = []
	# 26 27
	for i in range(87,28,-1):
		proxies2 = get_ip()		
		print(proxies2)

		Volume_req = requests.get('https://www.sciencedirect.com/journal/journal-of-fluids-and-structures/vol/{0}/suppl/C'.format(i), headers=HEADERS,proxies=proxies2)
		Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
		Article  = Volumesoup.find_all('a',{"class":"anchor article-content-title u-margin-xs-top u-margin-s-bottom"})
		for j in Article:
			Article_sort.append(j.get('href'))
	num= 81
	proxies3 = get_ip()
	for i in range(81,len(Article_sort)):
		num= num+1
		print(num)
		print(baseurl+Article_sort[i])
		inurl = baseurl+Article_sort[i]
		if num % 5 == 0:
			proxies3 = get_ip()
		else:
			proxies3= proxies3
		get(inurl,csv_write,out,proxies3)
	print('over')
	out.close()
