print()
from bs4 import BeautifulSoup

# 문서 가져오기
with open("./RPAbasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())  # 자료확인

# 1. 태그명으로 찾기
# title = soup.title
# print("title : {}".format(title))
# print(f"title : {title}")
# print("title 내용 : {}".format(title.get_text()))
# print("title 부모 태그 : {}".format(title.parent))

# # h1 태그 찾기
# print(f"h1 : {soup.h1}")
# print(f"h1 내용 : {soup.h1.get_text()}")

# # h2 태그 찾기
# print(f"h2 : {soup.h2}")
# print(f"h2 내용 : {soup.h2.get_text()}")

# p 태그 찾기 : 어떤 p를 찾을껀지.
# p1 = soup.p  # 제일 처음에 있는 p 태그
# print(f"p : {p1}")
# print(f"p 내용 : {p1.get_text()}")
# print(f"p 태그 속성들 : {p1.attrs}")
# print(f"p 태그 특정 속성 값 : {p1['class']}")

# b 태그 찾기
# print(f"b : {soup.b}")
# print(f"b 내용 : {soup.b.get_text()}")

# a 태그 찾기
print(f"a : {soup.a}")  # 가장 처음에 만나는 a
print(f"a 내용 : {soup.a.get_text()}")

print()
