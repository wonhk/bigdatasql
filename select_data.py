import sqlite3

# sqlite db 파일 생성 및 연결
con = sqlite3.connect('dbdb.db')
# sql 문장을 실행시키기 위해 준비
cursor = con.cursor() 

sql = '''
SELECT count(*) FROM melon where artist = '임영웅'
'''
cursor.execute(sql) # sql 을 실행
# 하나의 데이터를 보기
# data = cursor.fetchone()
print(cursor.fetchone())

# 전체 데이터 보기
# all_data = cursor.fetchall()
# # print(all_data)

# for d in all_data:
#     print(f'{d[0]}위 {d[1]} - {d[2]}')