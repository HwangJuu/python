print()
# 위키백과 - 서울 지하철 노선 사진 저장

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

res = requests.get(
    "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
)

soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())  # 자료 확인

# 지하철 노선 사진 저장
# 장점은 쉽게 가지고 올 수 있고, 단점은 길게 따라옴
# #mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
# 첫번째 지하철 노선 사진
image1 = soup.select_one(
    "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
)
# print(image1)
# print(image1["src"])

# 이미지 다운로드 - urlretrieve

# 다운로드 경로
path = "./RPAbasic/crawl/download/"

# urlretrieve("이미지 원본 경로", "다운로드 받을 경로")
# urlretrieve("http:" + image1["src"], path + "subway1.jpg")
# print()

# 두번째 사진 - 우표
# 요소 찾고 url 찾기
# #mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img
image2 = soup.select_one(
    "#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img"
)
print(image2)
print(image2["src"])

# 다운로드하기
urlretrieve("http:" + image2["src"], path + "anniversiry.jpg")


print()
