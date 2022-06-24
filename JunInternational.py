import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 1200, 800)
        
        #입력 텍스트 
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)

        #버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.setTableWidgetData)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(1100, 600)
        self.tableWidget.setRowCount(50)  #행의 갯수 
        self.tableWidget.setColumnCount(2)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 1100)
        
        #self.setTableWidgetData()
        self.tableWidget.doubleClicked.connect(self.doubleClicked)

    def setTableWidgetData(self):
        row = 0
        #User-Agent를 조작하는 경우 
        hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}
        for n in range(0,5):
            #클리앙의 중고장터 주소 
            data ='https://jundome.co.kr/goods/goods_list.php?page=' + str(n) + "&cateCd=015"
            req = urllib.request.Request(data, 
                headers = hdr)
            data = urllib.request.urlopen(req).read()
            page = data.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, 'html.parser')
            
            list = soup.find_all("div", class_="thumbnail")

#            list = soup.find_all('a', attrs={'img src':'/data/goods'})

#<div class="item-display type-cart">
#     <div class="list">
#         <ul>
#             <li style="width:25%">
#                 <div class="space">
#                     <div class="thumbnail">
#                     <a href="../goods/goods_view.php?goodsNo=1000004021"> <img src="/data/goods/22/04/15/1000004021/1000004021_main_044.jpg" width="166" alt="(박스)구욘 슈가프리 초코칩 쿠키 150g" title="(박스)구욘 슈가프리 초코칩 쿠키 150g" class="middle">                                        <span class="hot">
                                          
#                                         </span>
#                             <span class="choice">
#                             <button type="button" class="wish btn-add-wish" data-goods-no="1000004021" data-goods-nm="(박스)구욘 슈가프리 초코칩 쿠키 150g" data-goods-price="22800.00" data-goods-image-src="/data/goods/22/04/15/1000004021/1000004021_main_044.jpg" data-optionfl="n" data-min-order-cnt="1" data-option-sno="" data-goods-image="" data-sales-unit="1" data-fixed-sales="option" data-fixed-order-cnt="option">찜하기</button>
#                             <button href="#optionViewLayer" type="button" class="cart btn-open-layer btn-add-cart" data-mode="cartIn" data-goods-no="1000004021">장바구니</button>
#                             </span>
#                     </a>

#<img src="/data/goods/22/03/13/1000003985/1000003985_main_032.jpg" 
# width="166" alt="(박스)참좋은식품) 밀펑과자 80g" title="(박스)참좋은식품) 밀펑과자 80g" class="middle">

            f = open("Jun.txt", "a+", encoding="utf-8")
            for item in list:
                try:
                    #title = item.find("a").text
                    link = item.find("title").text
                    title = link.find("title")
                    print(link)
                    # span = item.contents[3]
                    # title = item.text.strip()
                    # #라인에디터에 입력된 문자열 받아서 검색
                    # if (re.search(self.lineEdit.text(), title)):
                    #     title = title.replace("\t", "")
                    #     title = title.replace("\n", "")
                    #     print(title)
                    #     link = 'https://www.clien.net'  + item['href'] 
                    #     print(link.strip())
                    #     f.write(title+"\n")
                    #     f.write(link + "\n")
                    #     #행데이터로 출력 
                    #     self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
                    #     self.tableWidget.setItem(row, 1, QTableWidgetItem(link))
                    #     row += 1
                    #     print("row: ", row) 
                except:
                    pass
             
            f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open(url) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()



