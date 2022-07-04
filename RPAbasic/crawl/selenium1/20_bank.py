print()
# 환율변동 자동화

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get("https://www.kebhana.com/cont/mall/mall15/mall1503/index.jsp")
browser.maximize_window()

# 못찾아서 에러남.
# html 안에 들어가있음. iframe안에 들어있음
# iframe 안으로 들어가기
browser.switch_to.frame("bankIframe")

# 기간 환율변동 클릭
browser.find_element(
    By.XPATH, '//*[@id="inqFrm"]/table/tbody/tr[1]/td/span/p/label[3]'
).click()

# 시작일자(20220523)
start_date = browser.find_element(By.ID, "tmpInqStrDt_p")
start_date.clear()
start_date.send_keys("20220523")

# 내 방법
# date_start = browser.find_element(By.XPATH, '//*[@id="tmpInqStrDt_p"]')
# date_start.clear()
# date_start.send_keys("20220523")
time.sleep(1)

# 종료일자(20220622)
end_date = browser.find_element(By.ID, "tmpInqEndDt_p")
end_date.clear()
end_date.send_keys("20220622")

# #내 방법
# date_end = browser.find_element(By.XPATH, '//*[@id="tmpInqEndDt_p"]')
# date_end.clear()
# date_end.send_keys("20220622")
time.sleep(1)

# 통화선택 --> 유로 클릭
# browser.find_element(By.ID, "curCd").click()
# browser.find_element(By.XPATH, '//*[@id="curCd"]/option[3]').click()

# 강사님 방법
browser.find_element(By.ID, "curCd").send_keys("EUR:유로(유럽연합)")

# 고시 회차 --> 최종 클릭
browser.find_element(
    By.XPATH, '//*[@id="inqFrm"]/table/tbody/tr[6]/td/span/p/label[2]'
).click()


# 조회 버튼 클릭 - iframe안에 있음
browser.find_element(By.XPATH, '//*[@id="HANA_CONTENTS_DIV"]/div[2]/a/span').click()
time.sleep(1)

# 엑셀 다운로드 클릭
browser.find_element(By.XPATH, '//*[@id="searchContentDiv"]/div[1]/a[2]/span').click()


time.sleep(3)
browser.quit()


print()
