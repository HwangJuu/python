print()
from urllib.request import urlopen, Request
from fake_useragent import UserAgent

# 네이버 뉴스 기사 주소
url = "https://n.news.naver.com/mnews/article/346/0000051487?sid=101"

# try:
#     request_url = Request(url)
#     res = urlopen(request_url).read().decode("utf-8")
#     print(res)
#     print(request_url.header_items()) #[('Host', 'n.news.naver.com'), ('User-agent', 'Python-urllib/3.10')] : 파이썬 버전
# except Exception as e:
#     print(e)


try:
    userAgent = UserAgent()
    headers = {"user-agent": userAgent.chrome}

    request_url = Request(url, headers=headers)
    res = urlopen(request_url).read().decode("utf-8")
    # print(res) 내용 확인
    print(request_url.header_items())  # Chrome/27.0.1453.93 Safari/537.36') 크롬 버전으로 바뀜
except Exception as e:
    print(e)

print()
