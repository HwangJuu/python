print()
# 다나와 상품 자동화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")
browser.maximize_window()
time.sleep(1)

# # +27버튼 찾기
# element = browser.find_element(
#     By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'
# ).click()
# # APPLE 버튼 찾기
# apple = browser.find_element(By.ID, "searchMaker1452").click()

# 제조사 더보기 클릭
WebDriverWait(browser, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]')
    )
).click()

# Apple 버튼 클릭
browser.find_element(
    By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[17]/label'
).click()

# 제품 목록이 화면에 로딩되도록 대기
time.sleep(5)

# 자료가 잘 나오는지 확인 : 소스 확인
# print(browser.page_source)


# 상품 정보 추출 - 상품명, 가격(첫번째), 이미지 src 출력
# 상품 목록 리스트 가져오기
product_list = browser.find_elements(
    # 광고와 제일 마지막에 있는 비어있는 리스트는 제외
    By.CSS_SELECTOR,
    "div.main_prodlist_list > ul>  li:not(.prod_ad_item):not(.product-pot)",
)


# 현재 페이지 / 크롤링할 페이지 수 지정
cur_page, target_crawl_num = 1, 6

# 번호 출력
idx = 1


# 페이지 제어 총 6페이지
while cur_page <= target_crawl_num:

    # 셀레니움이 잘 안될 땐 BeautifulSoup
    # 매번 받아서 파싱
    soup = BeautifulSoup(browser.page_source, "lxml")

    product_list = soup.select(
        "div.main_prodlist_list > ul> li:not(.prod_ad_item):not(.product-pot)"
    )
    print(product_list)

    # 현재 페이지 출력
    print("=============Current Page : {}".format(cur_page))

    # 상품 정보 출력 1페이지당 30개
    for product in product_list:

        # 제품명
        # 셀레니움 : product_name = product.find_element(By.CSS_SELECTOR, "p > a").text.strip()
        product_name = product.select_one("p > a").text.strip()

        # 가격
        # 셀레니움 : product_price = product.find_element(
        #     By.CSS_SELECTOR, "p.price_sect > a"
        # ).text.strip()
        product_price = product.select_one("p.price_sect > a").text.strip()

        # 이미지 경로
        # 셀레니움 : product_image = product.find_element(By.CSS_SELECTOR, ".thumb_image img")
        product_image = product.select_one(".thumb_image img")

        # 셀레니움
        # if product_image.get_attribute("data-original"):
        #     product_image = product_image.get_attribute("data-original")
        # else:
        #     product_image = product_image.get_attribute("src")

        if product_image.get("data-original"):
            product_image = product_image.get("data-original")
        else:
            product_image = product_image.get("src")

        if "http:" not in product_image:
            product_image = "http:" + product_image

        print(idx, product_name, product_price, product_image)
        idx += 1
        # for문 종료

    print()  # 한페이지 끝남.

    browser.save_screenshot(
        "./RPAbasic/crawl/download/target_page{}.png".format(cur_page)
    )

    # 현재 페이지 번호 변경
    cur_page += 1

    if cur_page > target_crawl_num:
        print("크롤링 성공")
        break

    # 다음페이지 클릭
    # 페이지 클릭 시
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(2)
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(3)
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(4)
    # 페이지 변화 필요하기 위해 자리를 잡아두고 페이지 값 넣어주기
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(cur_page))
        )
    ).click()

    # soup 삭제
    del soup

    # 다음 페이지 로딩될 때까지 기다리기
    time.sleep(3)
    # while문 종료


time.sleep(3)
browser.quit()


print()
