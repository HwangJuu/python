print()

from urllib.request import urlopen
from urllib.parse import urlencode

# # 네이버에서 영화 검색
# # query=%EC%98%81%ED%99%94 == '영화' ==> 한글, 공백 문자 자동 인코딩
# url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94"
# # 에러 발생. 한글부분을 인식하지 못함
# url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=영화"


param = {"query": "영화"}

url = (
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&"
    + urlencode(param)
)


try:
    res = urlopen(url).read().decode("utf-8")
except:
    print("URL Error")
else:
    print(res)

print()
