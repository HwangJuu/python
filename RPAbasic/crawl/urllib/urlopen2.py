print()
import urllib.request as req

# 11번가에서 주소 가지고 오기
try:
    url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
    res = req.urlopen(url)
    # content = res.read().decode("utf-8") # 'utf-8' codec can't decode byte 0xb9 in position 141: invalid start byte
    # 11번가는 인코딩 방식이 charset = euc-kr로 되어 있음
    content = res.read().decode("euc-kr")
except Exception as e:
    print(e)
else:
    print(content[:3000])
    print(res.info())

print()
