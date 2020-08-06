import requests
import time
import requests
import datetime
from bs4 import BeautifulSoup


keyword = "헬스"
url = "https://platum.kr//?s=" + keyword

soup = requests.get(url).text
html = BeautifulSoup(soup, 'html.parser')

title_list = []
url_list = []
date_list = []
for i in range(3) :
    title_list.append(html.find_all('h5')[i].find('a')['title'])
    url_list.append(html.find_all('h5')[i].find('a')['href'])
    date_list.append(html.find_all('span', {"class" : "post_info_date"})[i].find('a').text)
    
    
title = title_list[0] 
url = url_list[0]
date = date_list[0]
content = {"title": title, "url":url, "date": date}

def main():
    # webhook url
    url = "https://hooks.slack.com/services/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"
    text = content
    payload = {"text": text}
    requests.post(url, json=payload)

# 이 스크립트에서 실행할 함수는 main
if __name__ == "__main__":
    main()