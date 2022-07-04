print()
# 영화진흥 위원회 어제 날짜 박스 오피스 파일 저장 - txt파일
import urllib.request as req


# 다운로드 받을 경로
path = "./RPAbasic/crawl/download/"


try:
    url = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20220608"
    contents = req.urlopen(url).read().decode("utf-8")  # 파일 읽기
except Exception as e:
    print(e)
else:
    # else에 안하고 try에 작성 가능
    with open(path + "movie.txt", "w", encoding="utf-8") as f:  # 파일 저장
        f.write(contents)

        print("성공")


print()
