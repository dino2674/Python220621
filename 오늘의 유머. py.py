# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일 생성 (기존 파일에 첨부)
f = open("c:\\work\\humor.txt", "a+", encoding="utf-8")

for n in range(1,11):
        #오늘의 유머 베스트 오브 게시판 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)

        #웹브라우져 헤더 추가 
        #헤더가 없으면 웹봇으로 인식할 수 있어서 넣어줘야 함
        req = urllib.request.Request(data, \
                                    headers = hdr)

        data = urllib.request.urlopen(req).read()

        #한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore')

        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})


#<td class="subject">
# <a href="/board/view.php?table=bestofbest&amp;no=456276&amp;s_no=456276&amp;page=10" target="_top">
# 세상은 메타버스라는 스님</a>

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 

                        title = item.find("a").text
                        #print(title.strip())
                        if (re.search('누리호', title)):
                            print(title.strip())
                            f.write(title.strip() + "\n")
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
f.close()
print("웹 크로링 종료")