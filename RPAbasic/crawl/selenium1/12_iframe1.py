print()
# iframe : 하나의 html 페이지에서 다른 html 페이지를 포함
# iframe 안에 있는 요소 찾기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_headers")
browser.maximize_window()
time.sleep(2)

# iframe 안의 태그 찾기
# iframe 안으로 들어가서 찾아야 함
browser.switch_to.frame("iframeResult")

element = browser.find_element(By.TAG_NAME, "h1")
# frame 전 에러 : NoSuchElementException: Message: no such element: Unable to locate element: {"method":"tag name","selector":"h1"}
print("h1 :", element.text)

# iframe 밖으로 나오기
browser.switch_to.default_content()

# 왼쪽에 있던 요소 찾기
left = browser.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[12]/span/span[10]',
)
print(left.text)


time.sleep(3)
browser.quit()


print()
