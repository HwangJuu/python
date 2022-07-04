print()
# 댓글
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome()
browser.get("https://news.v.daum.net/v/20220622143115368")
# browser.maximize_window()
time.sleep(3)

# 댓글을 확인 할 수 있도록 댓글 On 클릭
browser.find_element(By.CLASS_NAME, "btn_foldup").click()
time.sleep(5)

try:

    # 최신순 클릭 : 해당 태그가 있는지 검사(5초동안 ==> 요소를 못찾으면 TimeoutException 발생)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="alex-area"]/div/div/div/div[3]/ul[1]/li[3]/button')
        )
    ).click()
except TimeoutException:
    # 댓글이 없으면 최신순 버튼이 없음.
    print("요소 못 찾음")


loop, count = True, 0
# 더보기 10번 클릭
while loop and count < 10:
    try:
        # browser를 XPATH 요소를 찾는데 5초동안 기다림. 5초가 되기 전에 찾으면 실행됨.
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="alex-area"]/div/div/div/div[3]/div[3]/button')
            )
        ).click()

        count += 1
        time.sleep(2)

    except:
        print("요소 못 찾음")
        loop = False

# 댓글 영역을 가져온 후 화면 출력
# 댓글 내용 출력
comment_list = browser.find_elements(By.CSS_SELECTOR, "ul.list_comment > li")

for idx, comment in enumerate(comment_list, 1):
    content = comment.find_element(By.CSS_SELECTOR, "div p")
    print("[{}] : {}".format(idx, content.text))


time.sleep(3)
browser.quit()
