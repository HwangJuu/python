print()
# 전체 스크롤 스크립트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://shopping.naver.com/home/p/index.naver")
browser.maximize_window()
time.sleep(1)

# 검색창 찾기 : 마우스 검색어 넣기
element = browser.find_element(By.CLASS_NAME, "_searchInput_search_input_QXUFf")
element.send_keys("마우스")
# element.send_keys(Keys.ENTER) # 엔터가 안됨.

# 버튼 클릭
browser.find_element(By.CLASS_NAME, "_searchInput_button_search_1n1aw").click()

# 스크롤 이동 : window.scrollTo(x,y) 좌표 지점
# 고정 값을 주면 해상도에 따라 달라질 수 있음.
# 스크롤 움직이는지 확인. 특정 위치 값 지정.
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2160)")

# 브라우저 끝으로 이동, 동적으로 움직이기 때문에 끝이 아님. 반복 필요
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 동적 페이지 스크롤링
# 2초에 한번씩 스크롤 이동
interval = 2
# 현재 문서 높이 가져와서 저장
prev_height = browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

while True:
    # 스크롤 이동
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤이 진행된 후 현재 문서 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    prev_height = curr_height

# 다시 위로 이동
browser.execute_script("window.scrollTo(0,0)")


time.sleep(3)
browser.quit()


print()
