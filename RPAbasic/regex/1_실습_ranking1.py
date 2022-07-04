print()
# https://news.nate.com/rank/interest?sc=ent 연예 랭킹 뉴스 추출 + 엑셀 저장(nate_오늘날짜.xlsx)
# 시트명 : 연예랭킹 뉴스
# 제목, 기사제공자(연합뉴스...) 1~ 50위

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime  # 오늘 날짜
import re


# 엑셀 작업
# 엑셀 파일 생성
wb = Workbook()

# 기본 시트 활성화
ws = wb.active

# 시트명 새로 지정
ws.title = "연예랭킹 뉴스"

ws.column_dimensions["A"].width = 70
ws.column_dimensions["B"].width = 15

# 제목행 지정
ws.append(["기사 제목", "신문사"])

res = requests.get("https://news.nate.com/rank/interest?sc=ent")
soup = BeautifulSoup(res.text, "lxml")

# 1~5위 가져오기(타이틀, 기사작성자)

# div.postRankSubjectList.f_clear
top5_list = soup.select("div.mduSubjectList > div")
# print(top5_list)

# 6~50위 가져오기
top45_list = soup.select("#postRankSubject li")

for idx, news in enumerate(top5_list, 1):
    # 타이틀 == 자손 태그로 끌기
    title = news.select_one("a strong").get_text()
    # 신문사(신문사 날짜) - 한글, 영문 문자만 찾기 (마이데일리 2022-06-22)
    media_date = news.select_one("span.medium").get_text()

    # re.sub() 날짜를 공백으로 바꾸기
    pattern = re.compile("[\d-]+")  # 숫자와 - 찾기
    media = re.sub(pattern, "", media_date)
    print(f"{idx} : {title} - {media}")

    # # split() ==> 결과가 리스트로 뜸['마이데일리','2022-06-22']
    # media = pattern.split(media_date)
    # print(f"{idx} : {title} - {media[0]}")
    ws.append([title, media])

    # re.sub(), split() : 둘 중 한가지만 실행

for idx, news in enumerate(top45_list, 6):
    # 타이틀
    title = news.select_one("a").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
    ws.append([title, media])

# 기사 제목 가지고오기
# title_list = soup.select("newsContents > div > div.postRankSubjectList.f_clear")
# print(title_list)

# 파일명 nate_오늘날짜.xlsx
# 날짜별로 저장 되는지
today = datetime.now().strftime("%y%m%d")
filename = f"nate_{today}.xlsx"

# 엑셀 저장
wb.save("./RPAbasic/crawl/download/" + filename)
print()
