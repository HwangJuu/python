print()
# 네이버

import re
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com")
soup = BeautifulSoup(res.text, "lxml")

# h 태그로 시작하는 모든 태그 찾기
# h1 ~ h6
print(soup.find_all(re.compile("h\d")))  # h태그 뒤에 숫자

print()
# 이미지 파일을 가져오기 - 1.jpg, ex.jpg,
# .+\.jpg ==> . (모든문자) + (무조건하나는와야함) \.(확장자구별 점)
print(soup.find_all("img", attrs={"src": re.compile(".+\.jpg")}))  # 확장자가 jpg 끝나는
print(soup.find_all("img", attrs={"src": re.compile(".+\.jpg|png")}))  # jpg이나 png


print()
