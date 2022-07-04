print()
import requests
from bs4 import BeautifulSoup

# 다음에 있는 첫 뉴스 주소
res = requests.get("https://news.v.daum.net/v/20220613093413149")
# print(res.text)  # 자료확인

soup = BeautifulSoup(res.text, "lxml")

# 기사제목 가져오기
# 첫번째 있는 거라면 soup.h3도 가능
news_title = soup.find("h3")
print("기사 제목 : ", news_title)
print("기사 제목 내용 : ", news_title.get_text())
print()
# 기사 작성날짜와 시간 가져오기
num_date = soup.find("span", "num_date")
print("작성 날짜 및 시간 : ", num_date)
print("작성 날짜 및 시간  내용 : ", num_date.get_text())
print()
# 기사 작성자 가져오기
writer = soup.find("span", "txt_info")
print("작성자 : ", writer)
print("작성자 내용: ", writer.get_text())
print()
# 기사 첫번째 문단 가져오기
para1 = soup.find("p")
print("기사 첫 문단 : ", para1)
print("기사 첫 문단 내용 : ", para1.get_text())

print()
# 전체 기사 내용 가져오기. p태그
contents = soup.find_all("p")
# print(contents)
for para1 in contents:
    print(para1.get_text())

print()
