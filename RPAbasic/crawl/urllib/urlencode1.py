print()
from urllib.request import urlopen
from urllib.parse import urlencode

# 접속한 주소에 ip주소를 찍어줌.
api = "https://api.ipify.org"  # 페이지에 번호만 출력 121.160.42.16
# https://api.ipify.org/?format=json ==> key,value 형태로 바뀜. {"ip":"121.160.42.16"}

# url = api + "?" + "format=json"

values = {"format": "json"}  # 그냥 실행하면 하면 타입오류

# url = api + "?" + values #TypeError: can only concatenate str (not "dict") to str

url = api + "?" + urlencode(values)  # urlencode : 브라우저를 직접 띄워서 일어날수 있는 문제를 해결해줘야함.

res = urlopen(url).read().decode("utf-8")
print(res)


print()
