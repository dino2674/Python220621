# db2.py

import sqlite3

#연결 객체를 리턴받기 (파일에서 영구적으로 저장)
con = sqlite3.connect("c:\\work\\sample.db")

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

cur.execute("SELECT * FROM PhoneBook;") #메모리에서 삭제되기 때문에 다시 조회해야 모든 레코드가 조회 됨. 아니면 위와 같이 먼저 조회 후 All 하면 메모리에서 삭제 됐기 때문에 하나만 조회 됨
print(cur.fetchall())

# 작업을 정상적으로 완료
con.commit()



# for row in cur:
#     print("Name : " + row[0] + "\t" + "Phone Number : " + row[1] )

  