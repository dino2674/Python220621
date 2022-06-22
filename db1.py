# db1.py

import sqlite3

#연결 객체를 리턴받기 (일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")

#커서 객체를 리턴받기
cur = con.cursor()

#테이블 (스키마)를 생성
cur.execute("CREATE TABLE PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("INSERT INTO PhoneBook (Name, PhoneNum) VALUES ('derick', '010-222');")

#입력 파라미터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("INSERT INTO PhoneBook (Name, PhoneNum) VALUES (?, ?);", (name, phoneNumber)) # 튜플로 처리

#여러 건을 입력
detalist = (("tom", "010-123"), ("dsp", "010-456"))
cur.executemany("INSERT INTO PhoneBook (Name, PhoneNum) VALUES (?, ?);", detalist) # 튜플로 처리

# 검색
cur.execute("SELECT * FROM PhoneBook;")

for row in cur:
    print("Name : " + row[0] + "\t" + "Phone Number : " + row[1] )

  