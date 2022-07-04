print()
import requests

url = "https://api.github.com/events"

# url이 시간 안에 응답이 없다면 에러로 처리
res = requests.get(url, timeout=0.001)
print(res.text)

print()
