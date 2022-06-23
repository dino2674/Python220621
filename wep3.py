#wep2.py

import urllib.request
from bs4 import BeautifulSoup

#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

try:
    #동적으로 주소 생성
    for i in range(1, 10):
        
        #웹 페이지의 실행 결과를 문자열로 받기
        #줄 바꿈은 "\" 사용
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + \
            str(i)
        print(url)
        data = urllib.request.urlopen(url)

        soup = BeautifulSoup(data, "html.parser")


        # <td class="title">
        # 	<a href="/webtoon/detail?" >마음의 소리 50화 <격렬한 나의 하루></a>
        # </td>

        cartoons = soup.find_all("td", class_="title")
        # print("개수 : {0}".format(len(cartoons)))
        # title = cartoons[0].find("a").text
        # link = cartoons[0].find("a")["href"]
        # print(title)
        # print(link)

        for item in cartoons:
            title = item.find("a").text
            print(title.strip())
            f.write(title.strip() + "\n")
except:
    pass 

f.close()
print("웹 크롤링 종료")


