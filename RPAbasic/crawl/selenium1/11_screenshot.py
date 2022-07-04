print()
# 다음에서 검색 후 관련 검색어 추출하고 스크린샷
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()
time.sleep(2)

# 검색창 찾기
element = browser.find_element(By.NAME, "q")
# 검색어 넣기 + 엔터
element.send_keys("콘서트")
element.send_keys(Keys.ENTER)
time.sleep(2)

# 관련검색어 추출
lists_top = browser.find_elements(By.CSS_SELECTOR, "#netizen_lists_top > span.wsn")
for item in lists_top:
    print(item.text)

# 현재 화면 캡쳐 - 기본 캡쳐 방식.png, jpg==> 경고 메세지 뜸
browser.save_screenshot("./RPAbasic/crawl/download/image.png")


time.sleep(3)
browser.quit()

print()
