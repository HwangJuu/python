print()
import urllib.request as req

# 이미지, html 파일 다운로드
# 검색 후 이미지 주소 복사
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTRfMjIx%2FMDAxNjUyNTE3NDYwOTI5.N1XANvyVbrVCuMUk5h8jG9UuKx4wzn6hN7YgHNhkqtwg.qJ_25tjAdJSlmkmXlcXoAmBem4JRLfQqgYQWhtsBpokg.PNG.feelgoodkjg%2F20220514_173526.png&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./RPAbasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "cat.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)

print()
