print()
from fake_useragent import UserAgent
from urllib.request import urlopen


userAgent = UserAgent()  # 객체 생성

# 만들고 싶은 브라우저 형태로 만들어 낼 수 있음
print(userAgent.ie)
print(userAgent.msie)
print(userAgent.chrome)
print(userAgent.safari)
print(userAgent.opera)
print(userAgent.firefox)
print(userAgent.random)


print()
