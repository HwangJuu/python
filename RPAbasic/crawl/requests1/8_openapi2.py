print()
# 네이버 api를 이용한 도서 검색
# 도서명, link, 출판사, 출판일

import requests

client_id = "ITricAb_moCNCZRXqDKt"
client_secret = "i1dMkiMcjU"

url = "https://openapi.naver.com/v1/search/book.json"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

start, num = 1, 0
for idx in range(10):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/book.json?query=재테크&display=100&start="
        + str(start_num)
    )
    # print(url)

    res = requests.get(url, headers=headers)

    # json 데이터 확인
    # print(res.json())
    data = res.json()

    for item in data["items"]:
        num += 1
        print(num, item["title"], item["link"], item["publisher"], item["pubdate"])


print()
