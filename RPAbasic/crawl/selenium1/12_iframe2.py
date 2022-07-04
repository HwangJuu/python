print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
)
browser.maximize_window()
time.sleep(1)

# h1 태그 찾기
h1_element = browser.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[5]/span/span[4]',
)
print(h1_element.text)

# iframe 안의 태그 찾기
# iframe 안으로 들어가서 찾아야 함
browser.switch_to.frame("iframeResult")

# 첫번째 라디오 찾은 후 클릭
element = browser.find_element(By.XPATH, '//*[@id="html"]').click()

# 다른 방법 : browser.find_element(By.ID,"html").click


time.sleep(3)
browser.quit()


print()
