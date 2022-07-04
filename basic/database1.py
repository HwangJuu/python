print()
# db 연동

# 라이브러리 끌어올리기
import sqlite3  # 라이브러리 이름
from datetime import datetime

# print(sqlite3.version)  # 2.6.0
# print(sqlite3.sqlite_version)  # 3.37.2

# # 날짜 생성
now = datetime.now()
# print("now : ", now)
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")  # string format 지정
# print("now_date_time : ", now_date_time)

# 연결
# sql에서 create 한 것과 같음
conn = sqlite3.connect("data/database.db", isolation_level=None)

# 커서 : 데이터베이스 접근 할 수 있는 객체
cursor = conn.cursor()
print(type(cursor))  # <class 'sqlite3.Cursor'>

# 테이블 생성
# IF NOT EXISTS 테이블 한번만 생성
# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, phone text, website text, regdate text)"
# )

# insert
# 한개씩 삽입
cursor.execute(
    "INSERT INTO users VALUES(1,'Kim','010-1234-1234','kim.com',?)",
    (now_date_time,),  # tuple의 형태로 넣기 ? 값에 대해 튜플로 넣어야함.
)  # ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 19 supplied.

cursor.execute(
    "INSERT INTO users VALUES(?,?,?,?,?)",
    (2, "Hong", "010-1234-4567", "hong.com", now_date_time),
)

# 여러개 삽입. list 형태
user_list = (
    (3, "Park", "010-4567-1234", "park.com", now_date_time),
    (4, "Choi", "010-9876-1234", "choi.com", now_date_time),
    (5, "Yoo", "010-3687-1234", "yoo.com", now_date_time),
)
cursor.executemany("INSERT INTO users VALUES(?,?,?,?,?)", user_list)

print()
