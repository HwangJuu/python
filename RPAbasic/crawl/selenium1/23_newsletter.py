print()
# 네이버에서 뉴스 링크 추출하여 가입자에게 전송
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import requests

import pyperclip


browser = webdriver.Chrome()
browser.get("https://www.naver.com")
browser.maximize_window()
time.sleep(1)

# 새창으로 다음 띄우기
browser.execute_script("window.open('http://www.daum.net')")

# 브라우저 2개 리스트로 다루기
tabs = browser.window_handles  # tabs[0] : naver, tabs[1] : daum

# 첫번째 탭 선택
browser.switch_to.window(tabs[0])

# 검색어 넣기
keyword = "RPA 파이썬"
browser.find_element(By.NAME, "query").send_keys(keyword)

# 검색버튼 클릭
browser.find_element(By.ID, "search_btn").click()

# 검색 결과 기다리기
time.sleep(2)

# 뉴스 메뉴 클릭
browser.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()
time.sleep(1)

# 최신순 클릭
browser.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

# 뉴스 조회일 기준으로 뉴스 건수 가져오기
client_id = "ITricAb_moCNCZRXqDKt"
client_secret = "i1dMkiMcjU"

url = "https://openapi.naver.com/v1/search/news.json"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

# 검색어
param = {"query": keyword}
# json으로 받아옴
res = requests.get(url, headers=headers, params=param)
result = res.json()
print(result)

# 뉴스 총 건수
new_total_cnt = result.get("total")  # result['total']

# 뉴스 총 건수를 파일 저장 - 23_totalCnt.txt
# 1) 기존 뉴스 건수를 읽어와서 변수에 담기
path = "./RPAbasic/crawl/selenium1/23_totalCnt.txt"
with open(path, "r") as f:
    old_total_cnt = int(f.readline())

# 2) new_total_cnt 와 기존 뉴스 건수 비교 ==> 지난 뉴스 기사 건수의 차이 구하기(new_add_cnt)
# 147-0
if new_total_cnt > old_total_cnt:
    new_add_cnt = new_total_cnt - old_total_cnt
    # 3) new_total_cnt를 텍스트에 기록
    with open(path, "w") as f:
        f.write(str(new_total_cnt))
else:
    new_add_cnt = 0

# 페이지 수 지정
if new_add_cnt == 0:
    page_cnt = 0
else:
    page_cnt = new_add_cnt // 10 + 1

start, num = 1, 1
# 결과값을 메일로 전송
result = ""

if page_cnt > 0:
    for i in range(3):  # page_cnt

        # 페이지 수 계산
        start = start + (i * 10)

        url = "https://search.naver.com/search.naver?where=news&query=" + keyword
        url += "&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0"
        url += "&mynews=0&office_type=0&office_section_code=0&news_office_checked="
        url += "&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&start=" + str(start)
        # start = 페이지 시작값

        browser.get(url)

        # 뉴스 크롤링
        # 뉴스제목, 매체(신문사), 등록일, 원문 주소
        # 뉴스 전 영역
        news_area = browser.find_elements(By.CLASS_NAME, "news_area")

        for idx, news in enumerate(news_area):
            # 뉴스 제목 news_area 안에 a
            title = news.find_element(By.CLASS_NAME, "news_tit")
            # 매체
            press = news.find_element(By.CLASS_NAME, "press")
            # 등록일
            reg_date = news.find_element(
                By.CSS_SELECTOR, "div.news_info > div.info_group > span"
            )
            # 원문 주소
            href = title.get_attribute("href")

            print(
                "{},{},{},{},{}".format(
                    idx, title.text, press.text, reg_date.text, href
                )
            )

            result += "<div><p><a href='" + href + "'>" + title.text + "</a> "
            result += press.text + " " + reg_date.text + "</p></div>"

print(result)  # 뉴스 검색 결과 확인

# 다음에서 이메일 보내기
# 두번째 탭인 Daum으로 이동
browser.switch_to.window(tabs[1])

# 다음 로그인 - 카카오계정으로 로그인 클릭
browser.find_element(By.CLASS_NAME, "link_kakaoid").click()
# //*[@id="inner_login"]/a[1]
time.sleep(1)

# 아이디 입력
id = browser.find_element(By.ID, "id_email_2")
id.clear()
id.send_keys("bit.hjh.5")
time.sleep(1)


# 비밀번호 입력
pwd = browser.find_element(By.ID, "id_password_3")
pwd.clear()
pwd.send_keys("qetu1357(")
time.sleep(1)

# 로봇이 아닙니다 클릭


# 로그인 클릭
browser.find_element(By.CLASS_NAME, "btn_confirm").click()
time.sleep(2)

# 메일 클릭
# browser.find_element(By.CLASS_NAME, "link_basis").click()
browser.find_element(By.XPATH, '//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/a').click()
time.sleep(5)


# result 내용 copy
pyperclip.copy(result)

# 메일 쓰기 클릭
browser.find_element(By.CLASS_NAME, "btn_write").click()
time.sleep(2)

# 받는사람란에 이메일 입력
toEmail = browser.find_element(By.ID, "toTextarea")
toEmail.send_keys("zoiia@naver.com")
time.sleep(2)
toEmail.send_keys(Keys.ENTER)

# 제목 입력
mailSubject = browser.find_element(By.ID, "mailSubject")
mailSubject.send_keys("RPA 파이썬 뉴스")
time.sleep(2)
mailSubject.send_keys(Keys.ENTER)

# 하단의 HTML 탭 클릭
browser.find_element(By.CLASS_NAME, "btn_html").click()
time.sleep(3)

# 메일 내용 텍스트 박스 선택 후 복사해 놓은 뉴스 붙여넣기
browser.find_element(By.CSS_SELECTOR, ".tx-canvas textarea").send_keys(
    Keys.CONTROL, "v"
)
time.sleep(2)

# 보내기
browser.find_element(By.CLASS_NAME, "btn_toolbar.btn_write").click()


time.sleep(3)
browser.quit()

print()
