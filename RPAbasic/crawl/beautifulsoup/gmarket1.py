print()
import requests
from bs4 import BeautifulSoup

# G마켓 주소
url = "https://www.gmarket.co.kr"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 1차 카테고리 추출하기
one_depth = soup.find_all("a", class_="link__1depth-item", limit=9)
# print(one_depth)  # 자료확인
# print()
# for item in one_depth:
#     print(item.get_text())

# 2차 카테고리 추출
# item__2depth = soup.find_all("li", "list-item__2depth")
# for item in item__2depth:
#     print(item)

# 이름만 가지고 오기. 두번씩 가지고 오기 때문에 개수제한
item__2depth = soup.find_all("li", "list-item__2depth", limit=69)
# print("카테고리 개수 : ", len(item__2depth))  # 개수 알기
# for item in item__2depth:
#     # print(item)
#     print(item.get_text())

item__2depth = soup.find_all("li", "list-item__2depth")
print("카테고리 개수 : ", len(item__2depth))
for item in item__2depth:
    print(item.string)
# get_text() : 태그(자식태그 포함)가 가지고 있는 모든 문자열 가져오기
# string : 태그가 가지고 있는 문자열만 가져오기

# 링크 안에 있는 a 태그를 찾고 href만 가져오기
# for depth in item__2depth:
#     href = depth.find("a")["href"]
#     # print(href)
#     print(depth.get_text(), href)

# aspx : c# 개념

print()
