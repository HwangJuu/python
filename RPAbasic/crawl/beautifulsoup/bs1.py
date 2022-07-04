print()
# requests + beautifulsoup4
# 객체 생성 후 사용 가능
# 객체 생성(페이지소스, 파서)
# 파서 == lxml
import requests
from bs4 import BeautifulSoup

# 다음에 있는 첫 뉴스 주소
res = requests.get("https://news.v.daum.net/v/20220613093413149")
# print(res.text)  # 자료확인

# 객체 생성(페이지소스, 파서)
# parser : html.parser(기본- 설치 필요없음)
# soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")  # html 형식으로 바뀜 # c언어 기반으로 되어 있어 빠름.
# print(soup)  # print(res.text) 같은 값으로 출력
# print(soup.prettify())  # 줄 정렬이 되어 출력(들여쓰기)

# <head> 태그 안 내용 가져오기
# print(soup.head)

# <body> 태그 내용 가져오기
# print(soup.body)

# title 태그
print(soup.title)  # title
print(soup.title.name)  # 태그 명
print(soup.title.get_text())  # 태그 안 text
print(soup.title.string)  # 태그 안 text


print()
