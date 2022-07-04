print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.naver.com")
browser.maximize_window()
time.sleep(1)

# 두번째 탭을 연 후에 daum 접속
# 스크립트로 새창 열기
browser.execute_script("window.open('http://www.daum.net')")

# 현재 페이지는 어디인지 확인
print("1. title {} ".format(browser.title))  # Naver

# 현재 브라우저에 열린 탭 가져오기
tabs = browser.window_handles  # tabs[0] : 처음 접속 페이지

browser.switch_to.window(tabs[1])  # 코드 이후론 다음페이지로 이동
print("2. title {} ".format(browser.title))

element = browser.find_element(By.NAME, "q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(1)

# 네이버로 돌아오기
browser.switch_to.window(tabs[0])

time.sleep(3)
browser.quit()

print()
