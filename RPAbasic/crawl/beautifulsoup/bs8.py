print()

from importlib.resources import contents
import requests
from bs4 import BeautifulSoup

# 다음에 있는 첫 뉴스 주소
res = requests.get("https://news.v.daum.net/v/20220613093413149")
print(res.text)  # 자료확인

soup = BeautifulSoup(res.text, "lxml")

# # <head> 태그 안 내용 가져오기
# print(soup.head)

# # <body> 태그 내용 가져오기
# print(soup.body)

# # title 태그
# print(soup.title)
# print(soup.title.name)
# print(soup.title.get_text())
# print(soup.title.string)

# 기사제목 가져오기
news_title = soup.select_one("h3")
print(news_title)
print(news_title.get_text())

# 기사 작정 날짜와 시간 가져오기
num_date = soup.select_one("span.num_date")
print(num_date)
print(num_date.get_text())

# 기사 작성자 가져오기
writer = soup.select_one("span.txt_info")
print(writer)
print(writer.get_text())

# 기사 첫번째 문단 가져오기
para1 = soup.select_one("p")
print(para1)
print(para1.get_text())

print()

contents = soup.select("p")
for para1 in contents:
    print(para1.get_text())


print()
