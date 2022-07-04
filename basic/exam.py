print()
# data/word.txt 로드 한 후 단어들 섞기
# 섞은 단어들 중에서 하나를 뽑아서 화면에 출력
# 출력된 단어를 보고 사용자는 똑같이 타이핑 하는 프로그램


from datetime import datetime
import random
import time
import sqlite3


conn = sqlite3.connect("data/records.db", isolation_level=None)
cursor = conn.cursor()
# 테이블 생성
# autoincrement : 자동 증가
sql = """ create table if not exists records
(id integer primary key autoincrement, cnt integer, record text, regdate text)
"""
cursor.execute(sql)
# data/word.txt 로드한 후 words 리스트에 단어들 붙여넣기
words = []
with open("data/word.txt", "r", encoding="utf-8") as f:
    for w in f:
        # print(w)
        words.append(w.strip())

# print(words)

n = 1

input("Ready? Press Enter Key")  # 사용자에게 시작 메세지
#  시작 시간
start = time.time()  # 초 단위로 리턴(기준 날짜 1970-01-01 0:0:0이 지난 시간)

# 정답 개수
cnt = 0

while n <= 5:
    # 리스트 속의 단어 섞기
    random.shuffle(words)

    # 임의의 단어 추출 : choice
    q = random.choice(words)

    print()

    print("Question #{}".format(n))

    # 문제(단어) 보여주기
    print(q)
    # 사용자로부터 입력 받기
    x = input()
    # print("입력값 : ", x)

    # 사용자의 입력값과 문제가 일치하는지 확인
    # 일치한다면 Pass 글자 출력, 정답개수 추가
    if x.strip() == q.strip():  # 공백 제거
        print("Pass")
        cnt += 1
    # 일치하지 않는다면 Wrong 출력
    else:
        print("Wrong")

    n += 1

# 종료시간
end = time.time()
et = end - start
et = format(et, ".2f")

# 게임하는데 걸린 시간 출력
print("게임 시간 : {}초, 정답개수:{}".format(et, cnt))

# 정답 개수가 4개 이상이면 합격, 아니면 불합격
if cnt >= 4:
    print("합격")
else:
    print("불합격")

# 기록 삽입(정답 개수, 시간, 오늘 날짜)

# 현재 시간
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# insert
sql = "insert into records('cnt','record','regdate') values(?,?,?)"
cursor.execute(sql, (cnt, et, today))

# cursor.execute("delete from records")
# conn.commit()
print()
