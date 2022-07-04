print()

import sqlite3

conn = sqlite3.connect("data/database.db", isolation_level=None)

cursor = conn.cursor()


# 조회
sql = """ select * 
from users
"""
cursor.execute(sql)

# fetchone(), fetchmany(), fetchall()
# print("1", cursor.fetchone())  # select 결과로 나온 제일 첫번째 행

# print("2", cursor.fetchmany(size=2))  # 리스트 구조로 출력. 내부는 tuple.
# print()
# print("3", cursor.fetchall())

# for문 사용 전체 호출
# for row in cursor.fetchall():
#     print("rows ", row)

# order by 내림차순
# sql = """ select *
# from users order by id desc
# """
# cursor.execute(sql)

# for row in cursor.fetchall():
#     print("rows ", row)


# 특정 조회
# sql = """ select *
# from users where id = ?
# """
# # ?는 tuple로 처리
# cursor.execute(sql, (3,))

# for row in cursor.fetchall():  # fetchone도 가능. 한개만 출력
#     print("rows ", row)

# % 사용
# sql = """ select *
# from users where id = %s
# """
# param = 4
# cursor.execute(sql % param)

# for row in cursor.fetchall():
#     print("rows ", row)

# 딕셔너리 사용
# sql = """ select *
# from users where id = :id
# """

# cursor.execute(sql, {"id": 5})

# for row in cursor.fetchall():
#     print("rows ", row)


# in 사용
sql = """ select *
from users where id in(?,?)
"""
param = (1, 3)
cursor.execute(sql, param)

for row in cursor.fetchall():
    print("rows ", row)


print()
