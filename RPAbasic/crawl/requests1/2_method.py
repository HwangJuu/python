print()
# get(), post(), delete(), put() == REST 관련된 메소드
import requests

# 연습용 사이트 이용
# url = "https://httpbin.org/"  # A simple HTTP Request & Response Service.

# get 방식 - 주소에 ?~~ 따라가는 방식
# url = "https://httpbin.org/get"  # A simple HTTP Request & Response Service.
# # 파라메터 사용 - 주소줄에 같이 감
# param = {"name": "hong"}
# # parameter 없을 때
# # res = requests.get(url)
# res = requests.get(url, params=param)

# print(res.headers)
# print(res.text)


# post 방식 : 많은 내용의 data를 보내겠다. form 내용을 보냄.
# url = "https://httpbin.org/post"
# data = {"name": "hong"}

# res = requests.post(url, data=data)
# print(res.text)


# delete 방식
# url = "https://httpbin.org/delete"
# res = requests.delete(url)
# print(res.text)


# put 방식 - form데이터 필요
url = "https://httpbin.org/put"

data = {"name": "kim"}

res = requests.put(url, data=data)
print(res.text)


print()
