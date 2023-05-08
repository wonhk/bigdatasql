import sqlite3

# sqlite db 파일 생성 및 연결
con = sqlite3.connect('dbdb.db')
# sql 문장을 실행시키기 위해 준비
cursor = con.cursor() 

sql = '''
SELECT * FROM Person
'''
cursor.execute(sql) # sql 을 실행
# 하나의 데이터를 보기
# data = cursor.fetchone()
# print(data)

# 전체 데이터 보기
all_data = cursor.fetchall()
print(all_data)