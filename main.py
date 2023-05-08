import mylib
import dbdb

# 멜론 가져오기
m_list = mylib.melon()
print(m_list)
# 멜론에서 가져온 데이터 리스트를 DB에 넣기 위해
dbdb.save_data(m_list)