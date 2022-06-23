#wep2.py

import urllib.request
from bs4 import BeautifulSoup

    
#웹 페이지의 실행 결과를 문자열로 받기
rul = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="
data = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, "html.parser")


# <td class="title">
# 	<a href="/webtoon/detail?" >마음의 소리 50화 <격렬한 나의 하루></a>
# </td>

cartoons = soup.find_all("td", class_="title")
print("개수 : {0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find("a").text
    print(title.strip())
    f.write(title.strip() + "\n")

f.close()