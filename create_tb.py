import sqlite3

print(sqlite3.version) # 버전확인

# sqlite db 파일 생성 및 연결
con = sqlite3.connect('dbdb.db')
print(type(con))
cursor = con.cursor() # sql 문장을 실행시키기 위해 준비
'''
안녕
여러줄로 주석 또는 문장을 
할수 있다
'''
"한줄 문장"
# sql = '''
# CREATE TABLE "Person" (
#     "ID"    INTEGER NOT NULL,
#     "Name"  TEXT NOT NULL,
#     "Birthday"  TEXT,
#     PRIMARY KEY("ID" AUTOINCREMENT)
# )
# '''

sql = '''
CREATE TABLE "melon" (
    "rank"    INTEGER NOT NULL,
    "title"  TEXT NOT NULL,
    "artist"  TEXT NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql) # sql 을 실행
con.commit() # 적용
con.close()  # db닫기