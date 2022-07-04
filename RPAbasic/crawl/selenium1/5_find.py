print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://daum.net")
browser.maximize_window()

# 원하는 요소 찾기
element = browser.find_element(By.NAME, "q")
print(
    element
)  # <selenium.webdriver.remote.webelement.WebElement (session="44e5c34d77c1aefae5ac98a1c3c32d20", element="e0d596aa-1086-4545-b46d-85929d7ee47f")>

# 검색어 넣기
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

# 검색 결과 기다리기
time.sleep(1)

# 검색 결과가 뜨고 난뒤 뒤로 가기
browser.back()

time.sleep(3)
browser.quit()


print()
