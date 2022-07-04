print()
# 화면 안에 내부 스크롤 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/default.asp")
browser.maximize_window()
time.sleep(1)

# 내부 스크롤 이동
element = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/div/a[56]')

# ActionChain() : 여러 개의 액션을 수행할 경우 차례대로 저장한 후 수행
#               : 마우스 이동, 마우스 버튼 클릭, key press....

# 액션
actions = ActionChains(browser)

# 특정 요소 이동
actions.move_to_element(element).perform()


time.sleep(3)
browser.quit()


print()
