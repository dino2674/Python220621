# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        #헤더가 없으면 웹봇으로 인식할 수 있어서 넣어줘야 함
        req = urllib.request.Request(data, \
                                    headers = hdr)

        data = urllib.request.urlopen(req).read()

        #한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore')

        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})


# <div class="list_title " data-role="list-title" data-toggle-custom="dropdown"> 
#         <a class="list_subject" href="/service/board/sold/17350208?od=T31&amp;po=0&amp;category=0&amp;groupCd=" data-role="cut-string">
                        
#                                 <span class="category fixed" title="판매">판매</span>
#                 <span class="subject_fixed" data-role="list-title-text" title="아이패드 프로 12.9 5세대 (m1) 256g wifi 스그">
#                         아이패드 프로 12.9 5세대 (m1) 256g wifi 스그
#                 </span>
#         </a>
        
#         <span class="icon_pic fa fa-picture-o"></span>
# </div>
        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 

                        title = item.text
                        print(title.strip())
                        if (re.search('맥북', title)):
                                print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
