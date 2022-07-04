print()
# 저장하고 싶은 이미지
import urllib.request as req

# 이미지, html 파일 다운로드
# 검색 후 이미지 주소 복사
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMjA1MThfMjUg%2FMDAxNjUyODQyMjY3OTg0.KB3NaA2GK4vFYT02ix4H5izylj-kMiXL9OpetmR64xkg.d-yJCY3RWcFcQKcLGOFKIxE-aqJSSoOPXpLXfHDGvecg.JPEG%2FI9w99jQZzLNyo1kvPCJrHUd89RtQ.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./RPAbasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "maldives.png")

except Exception as e:
    print(e)
else:
    print(header1)
    print()


print()
