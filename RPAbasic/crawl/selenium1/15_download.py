print()
# 구글 이미지 다운로드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from urllib.request import urlretrieve  # 다운로드 전용(페이지, 이미지)

browser = webdriver.Chrome()
browser.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
browser.maximize_window()
time.sleep(1)

# 검색창 찾기 - python입력
element = browser.find_element(By.NAME, "q")
element.send_keys("python")
element.send_keys(Keys.ENTER)


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
        # 이미지 더보기 버튼 기능 추가
        try:
            # 결과 더보기 버튼 찾은 후 클릭
            browser.find_element(By.CLASS_NAME, "mye4qd").click()
        except:
            break

    prev_height = curr_height


# 화면에 나온 작은 이미지들
images = browser.find_elements(By.CSS_SELECTOR, "div.bRMDJf.islir > img")
count = 1
for image in images:
    try:  # 이미지 저장
        image.click()
        time.sleep(2)

        # 큰 이미지 요소 찾기
        imgUrl = browser.find_element(
            By.XPATH,
            '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img',
        ).get_attribute("src")
        # 파일 다운로드 경로
        urlretrieve(imgUrl, "./RPAbasic/crawl/image/" + str(count) + ".jpg")
        count += 1

    except Exception as e:
        print("이미지 저장 실패")

# 다시 위로 이동
browser.execute_script("window.scrollTo(0,0)")

# 멈추고 싶다면 TERMINAL 창에서 ctrl + c


time.sleep(3)
browser.quit()

print()
