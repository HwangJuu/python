print()
# css 선택자 이용한 요소 찾기 : select, select_one
from bs4 import BeautifulSoup

# 문서 가져오기
with open("./RPAbasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

# 타이틀 클래스 명 가진 태그 요소 가져오기
title = soup.select_one("p.title")
# print(title)
# print(title.get_text())

# id가 link1 인 태그 요소 가져오기
# id는 중복이 안되니 하나만 가져올 수 있음
link1 = soup.select_one("#link1")
# print(link1)
# print(link1.get_text())
# print(link1.string)

# a 태그 중 data-* 속성 태그요소 가져오기
link2 = soup.select_one("a[data-io='tillie']")
# print(link2)
# print(link2.get_text())

# p 클래스 안에 자식 태그 a 모두 가져오기
# > : 자식
# find_all(), select() : 리스트 형식 --> for문 돌리기
all_a = soup.select("p.story > a")  # 리스트 형식으로 보여줌
print(all_a)
print()
for link in all_a:
    print(link)
    print(link.get_text())

print()
