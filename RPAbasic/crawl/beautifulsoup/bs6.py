print()
from bs4 import BeautifulSoup

# 문서 가져오기
with open("./RPAbasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify()) # 자료확인

# 2. find ~~

# 첫번째 p 태그
# p1 = soup.p
p1 = soup.find("p")
# print(p1)

# 문서에서 원하는 부분 찾기. 구조 개념은 아님. 단독으로 찾는 방법
p2 = soup.find("p", class_="story")
# print(f"p 두번째 : {p2}")
# print(f"p 두번째 내용 : {p2.get_text()}")
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
a1 = soup.find("a")

# 두번째 a 찾기. 첫번째 a와 상관없이.
a2 = soup.find("a", id="link2")
# print(f"a 두번째 : {a2}")
# print(f"a 두번째 내용 : {a2.get_text()}")
# print(f"a 두번째 속성들 : {a2.attrs}")
# print(f"a 두번째 특정 속성 값 : {a2['id']}")

# 세번째 a
# class, id는 단독으로 사용가능
# a3 = soup.find("a", id="link3")
# a3 = soup.find("a", class_="sister", id="link3")
# # "data-io" 속성은 한꺼번에 묶어서 가능
# a3 = soup.find("a", attrs={"class": "sister", "id": "link3", "data-io": "tillie"})
# print(f"a 세번째 : {a3}")
# print(f"a 세번째 내용 : {a3.get_text()}")
# print(f"a 세번째 속성들 : {a3.attrs}")
# print(f"a 세번째 특정 속성 값 : {a3['href']}") # 링크 속성

# find_all() : 모두 가져오기(리스트 값으로 돌아옴). 값이 하나여도 무조건 리스트로 출력

# a 찾기
a = soup.find_all("a")
# print(a) # 값이 3개

# b 찾기
b = soup.find_all("b")
# print(b)  # 값이 1개

# limit : 개수 지정해서 가지고 오기
a = soup.find_all("a", limit=2)
# print(a)

a = soup.find_all("a", class_="sister")
# print(a)

# 텍스트 노드 값 이용해서 가져오기
a = soup.find_all(string=["Elsie"])
print(a)
a = soup.find_all(string=["Elsie", "Lacie"])
print(a)

print()
