print()
# 다나와 사이트 로그인하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.danawa.com/")

browser.maximize_window()
time.sleep(1)

# 로그인 버튼 찾기
login = browser.find_element(By.CLASS_NAME, "btn_user--login")
login.click()

# 페이지 이동이 있으니 시간
time.sleep(1)

# 아이디 입력 찾기
userid = browser.find_element(By.ID, "danawa-member-login-input-id")
userid.clear()
# userid.send_keys("본인 아이디")
userid.send_keys("zoiia6263")

# 비밀번호 입력 찾기
password = browser.find_element(By.ID, "danawa-member-login-input-pwd")
password.clear()
# password.send_keys("본인비밀번호")
password.send_keys("abcd1234!")
password.send_keys(Keys.ENTER)


time.sleep(3)
browser.quit()

print()
