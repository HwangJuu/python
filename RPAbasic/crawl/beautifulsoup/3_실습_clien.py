print()
# clien 팁과 강좌 게시판 크롤링

import requests
from bs4 import BeautifulSoup

# res = requests.get("https://www.clien.net/service/board/lecture")
# soup = BeautifulSoup(res.text, "lxml")

# 게시판 제목 가져오기
# div_content > div.list_content > div:nth-child(18) > div.list_title > a.list_subject > span.subject_fixed
# 출력했을 때 안나오면 select 한개씩 추가
# title_list = soup.select(" a.list_subject > span.subject_fixed")
# print(title_list)
# for title in title_list:
#     print(title.get_text().strip())


# 1 ~ 5 page 목록 가지고 오기
for page_num in range(5):  # range : 0~4
    if page_num == 0:  # 1page
        res = requests.get("https://www.clien.net/service/board/lecture")
    else:
        res = requests.get(
            "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
            + str(page_num)  # 파이썬은 문자로 변경해줘야함.
        )
    soup = BeautifulSoup(res.text, "lxml")
    title_list = soup.select("a.list_subject > span.subject_fixed")
    for title in title_list:
        print(title.get_text().strip())
    print("*" * 80)  # 페이지 나누기 구분


print()
