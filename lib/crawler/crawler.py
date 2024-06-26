import requests
import io
from os.path import exists, isfile
from lib.helper.Log import *
from lib.helper.helper import *
from lib.core import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing import Process
#from threading import Thread

class crawler:
	
	threads = list()
	visited=[]
	
	@classmethod
	def getLinks(self,base,proxy,headers,cookie):

		lst=[]
	
		conn=session(proxy,headers,cookie)
		text=conn.get(base).text
		isi=BeautifulSoup(text,"html.parser")
	
		
		for obj in isi.find_all("a",href=True):
			url=obj["href"]
			
			
			if urljoin(base,url) in self.visited: #or not self.checker(urljoin(base,url)):
				continue

			elif url.lower().startswith("mailto:") or url.lower().startswith("javascript:"):
				continue
	# :// will check if there any subdomain or any other domain but it will pass directory		
			elif url.startswith(base) or "://" not in url :
				lst.append(urljoin(base,url))
				self.visited.append(urljoin(base,url))
			
		return lst

	@classmethod
	def checker(self, url, file="xss.txt"):
		if exists(file) and isfile(file):
			try:
				with io.open(file, "r") as f:
					content = f.read()
					f.close()
				if url in content.split("\n"):
					return False
				else:
					return True
			except FileNotFoundError:
				return True
	
	@classmethod
	def crawl(self, url, depth,thread, proxy, headers,level,method, cookie, random_agent, base=None):

		base = base if base else url
		urls=self.getLinks(base, proxy, headers, cookie)
		
		for url in urls:
			if url.lower().startswith("https://") or url.lower().startswith("http://"):
				p=Process(target=core.main, args=(url,proxy,headers,level,cookie,method, random_agent))
				p.start()
				if len(self.threads) > thread:
					for n, _ in enumerate(self.threads):
						_.join()
						self.threads.pop(n)
				else:
					self.threads.append(p)

				if depth != 0:
					self.crawl(url, depth-1, thread,proxy, headers, level, method, cookie, random_agent, base=base)
					
				else:
					break	
