print()
# https://news.nate.com/rank/interest?sc=ent 연예 랭킹 뉴스 추출
# 제목, 기사제공자(연합뉴스...) 1~ 50위

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.nate.com/rank/interest?sc=ent")
soup = BeautifulSoup(res.text, "lxml")

# 1~5위 가져오기(타이틀, 기사 작성자)
# div.postRankSubjectList.f_clear : 1위에서 5위까지
top5_list = soup.select("div.mduSubjectList > div")
# print(top5_list)

# 6~50위 가져오기
# #postRankSubject li : 6위에서 50위까지
top45_list = soup.select("#postRankSubject li")

for idx, news in enumerate(top5_list, 1):
    # 타이틀 (div > a> span> strong) == 자손태그로 끌면 하나라서 가능
    title = news.select_one("a strong").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")

for idx, news in enumerate(top45_list, 6):
    # 타이틀
    title = news.select_one("a").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")

# 기사 제목 가지고오기
# title_list = soup.select("newsContents > div > div.postRankSubjectList.f_clear")
# print(title_list)


print()
