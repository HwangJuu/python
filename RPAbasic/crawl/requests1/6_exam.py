print()
# 다음 쇼핑 베스트 100

import requests
from fake_useragent import UserAgent

# F12 : Elements에 있는데 sources에 없으면 동적으로 내려온 데이터
# 100개의 데이터 가지고 오는 소스 찾기 ==> Fetch/XHR
# Headers 확인에서 데이터 주소 가지고 올 수 있는지 확인


url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1654833610975"


# 순위, 제품명
res = requests.get(url)
# print(res.text) # 자료 확인

for idx, item in enumerate(res.json(), 1):
    print(idx, item["product_name"])


print()
