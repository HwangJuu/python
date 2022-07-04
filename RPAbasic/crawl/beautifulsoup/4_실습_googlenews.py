print()
# 구글 뉴스 클리핑(조각내서 가지고 오기)

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://news.google.com/search?q=파이썬&hl=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    news_clipping = data_extract(soup)

    for section in news_clipping:
        for k, v in section.items():
            print("{} : {}".format(k, v))
        print()


def data_extract(soup):
    # 원하는 요소 추출

    news_list = []  # 비어있는 리스트 생성
    news_item = {}  # dict 구조 생성

    # 뉴스 원문 url, 제목, 출처, 등록 일시 ==> 리스트 구조
    # 각 개별 기사는 dict 구조로 생성
    articles = soup.select("div.xrnccd > article")

    for article in articles:
        # print(article) # 개별로 뉴스 기사가 나오는지 확인
        # 제목과 링크를 가지고 있는 태그 요소 찾기
        link_title = article.select_one("h3 > a")

        # 기본 주소 설정
        base_url = "https://news.google.com"

        # 기본 주소 + 상대주소
        #  ./articles/CBMiN2h0dHBz~~~ ==> https://news.google.com/articles~~~
        news_item["href"] = (
            base_url + link_title["href"][1:]
        )  # ./articles/~~ => .뒤에 있는 부분부터
        news_item["title"] = link_title.get_text()

        # 출처와 뉴스보도 시간을 가지고 있는 요소 찾기
        writer_time = article.select_one("div.SVJrMe")

        # 출처만 추출
        news_item["writer"] = writer_time.select_one("a").get_text()

        # 시간만 추출
        date_time = writer_time.select_one("time")
        # <time class="WW6dff uQIVzc Sksgp" datetime="2022-06-14T00:50:53Z">2시간 전</time>

        if date_time:
            report_date_time = date_time["datetime"].split("T")
            report_date = report_date_time[0]
            report_date = report_date_time[1]
        else:
            report_date = ""
            report_time = ""

        news_list.append(news_item)
        news_item = {}

    # 리스트 리턴
    return news_list


if __name__ == "__main__":
    main()

print()
