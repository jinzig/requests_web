import requests
from bs4 import BeautifulSoup
se = requests.Session()

url = 'https://www.linkedin.com/uas/login-submit'
url_2 = 'https://www.linkedin.com/in/jinziguang?trk=hp-identity-name'
login_data = {
    'session_key':'jinzig@gmail.com',
    'session_password':'0451gznij'
}
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
s = se.post(url, login_data)
print(s)
html_loginpg = se.get('https://www.linkedin.com/in/jinziguang?trk=hp-identity-name', headers = headers)
html_page = html_loginpg.text
content = BeautifulSoup(html_page, 'html.parser').contents
print(content)