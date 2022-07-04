print()
# python.org 접속
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.python.org")
browser.maximize_window()

# 타이틀이 Python이 아니면 오류 발생
assert "Python" in browser.title

print("소스 가져오기")
print(browser.page_source)


time.sleep(3)
browser.quit()

print()
