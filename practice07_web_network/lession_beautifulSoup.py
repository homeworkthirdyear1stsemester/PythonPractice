from bs4 import BeautifulSoup  # 해당 tag를 읽어 오는 역할을 한다
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')

title = soup.find_all('title')
print(title)
