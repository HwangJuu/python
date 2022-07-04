print()
import sqlite3

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# 수정
# id가 2번인 user 이름을 cho로 변경

# sql = """ update users
# set username = ? where id = ?
# """
# cursor.execute(sql, ("cho", 2))
# conn.commit()

# 딕셔너리 구조
# sql = """ update users
# set username = :username where id = :id
# """
# cursor.execute(sql, {"username": "hong", "id": 2})
# conn.commit()

# format
# set username = %s where id = %s ==>  OperationalError: no such column: cho
# 홑 따옴표 사용
# sql = """ update users
# set username = '%s' where id = '%s'
# """
# cursor.execute(sql % ("cho", 2))
# conn.commit()


# delete
# 튜플
cursor.execute("delete from users where id=?", (2,))
# 딕셔너리
cursor.execute("delete from users where id=:id", {"id": 3})
# 포맷
cursor.execute("delete from users where id= %d" % 4)
conn.commit()


print()
