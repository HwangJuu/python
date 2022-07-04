print()
import urllib.request as req

# urlretrieve2.py에서 사용한 경로
target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTRfMjIx%2FMDAxNjUyNTE3NDYwOTI5.N1XANvyVbrVCuMUk5h8jG9UuKx4wzn6hN7YgHNhkqtwg.qJ_25tjAdJSlmkmXlcXoAmBem4JRLfQqgYQWhtsBpokg.PNG.feelgoodkjg%2F20220514_173526.png&type=sc960_832",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = [
    "./RPAbasic/crawl/download/cat.png",
    "./RPAbasic/crawl/download/naver.html",
]
# 오픈해서 데이터 저장까지


for i, url in enumerate(target_url):

    try:
        res = req.urlopen(url)

        contents = res.read()

        print("-----------------")
        print("Header info - {} : {}".format(i, res.info()))
        print("http status : {}".format(res.getcode()))
        print("-----------------")

        # 파일 저장코드. wb : 이미지라서 사용
        with open(path_list[i], "wb") as c:
            c.write(contents)
    except Exception as e:
        print(e)
    else:
        print("성공")

print()
