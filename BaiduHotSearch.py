import requests
from bs4 import BeautifulSoup

url = 'https://top.baidu.com/board?tab=realtime'
sourceCode = requests.get(url)
soup = BeautifulSoup(sourceCode.text,'lxml')
titles = soup.select('#sanRoot > main > div.container.right-container_2EFJr > div > div > div > div.content_1YWBm > a > div.c-single-text-ellipsis')
links = soup.select('#sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div > div.content_1YWBm > a')
for title,link in zip(titles,links):
    data = {
        'title':title.get_text(),
        'link':link.get('href')
    }
    print(data)
