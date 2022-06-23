# DemoForm2.py
# DemoFrom2.ui(디자인) + DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹 크로링
import urllib.request
from bs4 import BeautifulSoup

#디자인 파일 로딩
#대부분 ui 태그가 하나가 존재하는데 간혹 2개 이상일 수 있어서 0번째 조회
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의 (QMainWindow)
class DemoForm(QMainWindow, form_class):
    #생성자 메서드
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
    # 슬롯 메서드 정의
    def FirstClick(self):

        #파일로 저장
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

        try:
            #동적으로 주소 생성
            for i in range(1, 6):
                
                #웹 페이지의 실행 결과를 문자열로 받기
                #줄 바꿈은 "\" 사용
                url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + \
                    str(i)
                data = urllib.request.urlopen(url)

                soup = BeautifulSoup(data, "html.parser")
                cartoons = soup.find_all("td", class_="title")

                for item in cartoons:
                    title = item.find("a").text
                    print(title.strip())
                    f.write(title.strip() + "\n")
        except:
            pass 

        f.close()
        self.label.setText("네이버 웹툰 크로링 종료")

    def SecondClick(self):
        self.label.setText("두 번째 버튼~~")

    def ThirdClick(self):
        self.label.setText("세 번째 버튼~~")        

#진입점 체크
if __name__ == "__main__":

    # 실행 프로세스
    app = QApplication(sys.argv)

    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show()

    #이벤트 처리 대기
    app.exec_()