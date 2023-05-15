import sqlite3

# 데이터 넣기 함수
def save_data(m_list):
    # sqlite db 파일 생성 및 연결
    con = sqlite3.connect('dbdb.db')
    # sql 문장을 실행시키기 위해 준비
    cursor = con.cursor()
    sql = '''
    INSERT INTO melon (title, artist)
    VALUES (?, ?)
    '''
    cursor.executemany(sql, m_list) # sql 을 실행
    con.commit() # 적용
    con.close()  # db닫기

# 데이터 보기 함수
def get_data():
    # sqlite db 파일 생성 및 연결
    con = sqlite3.connect('dbdb.db')
    # sql 문장을 실행시키기 위해 준비
    cursor = con.cursor() 

    sql = '''
    SELECT * FROM melon
    '''
    cursor.execute(sql) # sql 을 실행
    # 하나의 데이터를 보기
    # data = cursor.fetchone()
    # print(data)

    # 전체 데이터 보기
    all_data = cursor.fetchall()
    print(all_data)
    con.close()  # db닫기
    return all_data


# 데이터 가수 검색 함수
def get_one_data(artist):
    # sqlite db 파일 생성 및 연결
    con = sqlite3.connect('dbdb.db')
    # sql 문장을 실행시키기 위해 준비
    cursor = con.cursor() 

    sql = f'''
    SELECT * FROM melon WHERE artist LIKE ?
    '''
    cursor.execute(sql, (f"%{artist}%", )) # sql 을 실행
    # 전체 데이터 보기
    all_data = cursor.fetchall()
    con.close()  # db닫기
    return all_data

# 테이블 삭제하는 함수
def drop_tb():
    con = sqlite3.connect('dbdb.db')
    cursor = con.cursor() # sql 문장을 실행시키기 위해 준비
    sql = '''
        DROP TABLE melon
    '''
    cursor.execute(sql) # sql 을 실행
    con.commit() # 적용
    con.close()  # db닫기



# 테이블 생성하는 함수
def create_tb():
    con = sqlite3.connect('dbdb.db')
    print(type(con))
    cursor = con.cursor() # sql 문장을 실행시키기 위해 준비
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



# 위 함수를 만들고 1번을 누르면 멜론 데이터 갱신하는것을 만들어 보자