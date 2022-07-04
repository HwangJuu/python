print()
from bs4 import BeautifulSoup

# 문서 가져오기
with open("./RPAbasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())  # 자료확인

# 2. find ~~

# 첫번째 p 태그
# p1 = soup.p
p1 = soup.find("p", "title")  # soup.find("p", class_="title")
# print(p1)

# 형제 p 태그 찾기
# 찾아놓은 기반으로 그 다음 태그 찾기
p2 = p1.find_next_sibling("p")
# print(f"p 두번째 : {p2}")
# print(f"p 두번째 내용 : {p2.get_text()}")# p가 가지고 있지 않은 자식들이 가지고 있는 내용도 출력됨
# print(f"p 두번째 속성들 : {p2.attrs}")
# print(f"p 두번째 특정 속성 값 : {p2['class']}")

# 세번째 p 찾기
# p3 = p2.next_sibling.next_sibling
p3 = p2.find_next_sibling("p")
# print(f"p 세번째 : {p3}")
# print(f"p 세번째 내용 : {p3.get_text()}")
# print(f"p 세번째 속성들 : {p3.attrs}")
# print(f"p 세번째 특정 속성 값 : {p3['class']}")

# 첫번째 a 태그 찾기
a1 = soup.a

# 두번째 a 찾기
a2 = a1.find_next_sibling("a")
# print(f"a 두번째 : {a2}")
# print(f"a 두번째 내용 : {a2.get_text()}")
# print(f"a 두번째 속성들 : {a2.attrs}")
# print(f"a 두번째 특정 속성 값 : {a2['id']}") # id 값 가지고 오기

# 앞쪽에 있는 요소 찾기 : find_previous_sibling
# p2의 앞쪽에 있는 태그 찾기
p1 = p2.find_previous_sibling("p")
print(f"p1 : {p1}")
print(f"p1 내용 : {p1.get_text()}")
print(f"p1 태그 속성들 : {p1.attrs}")
print(f"p1 태그 특정 속성 값 : {p1['class']}")

# 속성으로 되어 있는 내용 가지고오기
for v in p2.next_element:
    print(v, end="")

print()
