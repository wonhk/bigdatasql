import mylib
import dbdb

# 멜론 가져오기
# m_list = mylib.melon()
# print(m_list)
# 멜론에서 가져온 데이터 리스트를 DB에 넣기 위해
# # dbdb.save_data(m_list)
print('가수 이름으로 검색')
artist = input('가수이름입력: ')
m_list = dbdb.get_one_data(artist)
for m in m_list:
    print(f'{m[0]}위 {m[1]} - {m[2]}')
