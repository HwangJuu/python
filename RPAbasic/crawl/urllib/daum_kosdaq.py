print()
# 다음 증권 사이트 - 인기 검색

from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json
import csv


# html 태그가 출력됨.  인기 검색은 들어있지 않음. 동적으로 넣어서 나오지 않음.
# try:
#     url = "https://finance.daum.net/"
#     res = urlopen(url).read().decode("utf-8")
#     print(res)
# except Exception as e:
#     print(e)


headers = {"user-agent": UserAgent().chrome, "referer": "https://finance.daum.net/"}
# 다운로드 기본경로
path = "./RPAbasic/crawl/download/"
# 빈 리스트 생성
data = []

try:
    url = "https://finance.daum.net/api/search/ranks?limit=10"  # 그냥 들어가면 403에러
    res = urlopen(Request(url, headers=headers)).read().decode("utf-8")
    # print(res) # 자료 확인

    # json ==> dict 구조 변경
    rank_json = json.loads(res)["data"]

    for item in rank_json:
        print(
            "순위 {}, 금액 {}, 회사명 {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )
        data.append(item)

        with open(path + "finanace.txt", "a", encoding="utf-8") as txt, open(
            path + "finanace.csv", "a", encoding="utf-8", newline=""
        ) as csvfile:

            # 텍스트 저장
            txt.write(
                "순위 {}, 금액 {}, 회사명 {}\n".format(
                    item["rank"], item["tradePrice"], item["name"]
                )
            )

            # csv 저장
            output = csv.writer(csvfile)
            # 헤더명
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())  # value 저장

except Exception as e:
    print(e)


print()
