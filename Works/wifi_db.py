import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', 
                       user='admin', 
                       password='1111', 
                       db='rpa', 
                       charset='utf8')

cursor = conn.cursor()
query = "select * from wifi"
cursor.execute(query)

rows = cursor.fetchall()
print(rows)

import openpyxl as op
wb = op.load_workbook('./wifi.xlsx')

ws = wb['wifi_list']

data = []

for r in ws.rows:
    install_name = r[1].value
    install_addr = r[2].value
    install_category = r[3].value
    install_company = r[4].value
    
    data.append([install_name, install_addr, install_category, install_company])

try:
    cursor = conn.cursor()
    query = "INSERT INTO wifi (install_name, install_addr, install_category, install_company) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, data[1:])
    conn.commit()
    print("[+] Insertion success\n")
    
    conn.close()
    
except pymysql.err.InternalError as e:
    code, msg = e.args
    print(msg)
    print("[ERROR] Insertion failed\n")