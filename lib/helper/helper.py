'''
XSSCon - 2019/2024
This project was created by Ahmed AL-Nassif. 
Copyright under the MIT license
'''

import requests, json
from fake_useragent import UserAgent

##### Colors ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
##### Styling ######
underline = "\033[4m"
##### Default ######
ua = UserAgent(["chrome"])
agent = {'User-Agent': ua.random} 
line="—————————————————" 
#####################
def session(proxies,headers,cookie):
	r=requests.Session()
	r.proxies=proxies
	r.headers.update(headers)
	r.verify=False
	r.cookies.update(json.loads(cookie))
	return r

logo=G+"""██████╗ ██╗    ██╗███╗   ██╗██╗  ██╗███████╗███████╗
██╔══██╗██║    ██║████╗  ██║╚██╗██╔╝██╔════╝██╔════╝
██████╔╝██║ █╗ ██║██╔██╗ ██║ ╚███╔╝ ███████╗███████╗ %s
██╔═══╝ ██║███╗██║██║╚██╗██║ ██╔██╗ ╚════██║╚════██║ %s
██║     ╚███╔███╔╝██║ ╚████║██╔╝ ██╗███████║███████║
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
<<<<<<< STARTING >>>>>>>
"""%(R+"{v1.0 Final}"+G,underline+C+"https://github.com/ahmed-alnassif/PwnXSS"+N+G)
	
##=======
"""%(R+"{v1.0 Final}"+G,underline+C+"https://github.com/ahmed-alnassif/PwnXSS"+N+G)
	
>>>>>>> branch 'master' of https://github.com/ahmed-alnassif/PwnXSS
"""
