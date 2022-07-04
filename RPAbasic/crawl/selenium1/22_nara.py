print()
# 나라장터 용역 공고 자동화 + 엑셀
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


from openpyxl import Workbook

# 엑셀
# 업무,공고번호, 분류,공고명,공고기관,수요기관,계약방법,입력일시,입찰마감일시, 원문상세주소
wb = Workbook()

# 기본 시트 활성화
ws = wb.active

# 시트명 새로 지정
ws.title = "나라장터 용역공고"

# 타이틀 행 추가
ws.append(
    ["업무", "공고번호", "분류", "공고명", "공고기관", "수요기관", "계약방법", "입력일시", "입찰마감일시", "원문상세주소"]
)

# url 구별
# taskClCds=5 용역에 대한 정보만 불러오기
# fromBidDt : 시작 날짜, toBidDt : 끝날짜, currentPageNo : 페이지 나누기


browser = webdriver.Chrome()

# url 3번 조회
for i in range(1, 4):
    url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&areaNm=&bidNm=&"
    url += "bidSearchType=1&budgetCompare=&detailPrdnm=&detailPrdnmNo=&downBudget=&"
    url += "fromBidDt=2022%2F05%2F24&fromOpenBidDt=&industry=&industryCd=&instNm=&"
    url += "instSearchRangeType=&intbidYn=&orgArea=&procmntReqNo=&radOrgan=1&"
    url += "recordCountPerPage=30&refNo=&regYn=Y&searchDtType=1&searchType=1&"
    url += "strArea=&taskClCds=5&toBidDt=2022%2F06%2F23&toOpenBidDt=&upBudget=&"
    url += "currentPageNo=" + str(i) + "&maxPageViewNoByWshan=2&"

    browser.get(url)
    browser.maximize_window()

    # 업무,공고번호, 분류,공고명,공고기관,수요기관,계약방법,입력일시(입찰마감일시)
    tbody = browser.find_element(By.XPATH, '//*[@id="resultForm"]/div[2]/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    # td, tr로 구분이 어렵고 전체를 불러와서 순서를 정해서 가지고 오기
    for idx, row in enumerate(trs):
        # 업무
        data_1 = row.find_elements(By.TAG_NAME, "td")[0]
        # 공고번호
        data_2 = row.find_elements(By.TAG_NAME, "td")[1]
        # 분류
        data_3 = row.find_elements(By.TAG_NAME, "td")[2]
        # 공고명
        data_4 = row.find_elements(By.TAG_NAME, "td")[3]
        # 공고기관
        data_5 = row.find_elements(By.TAG_NAME, "td")[4]
        # 수요기관
        data_6 = row.find_elements(By.TAG_NAME, "td")[5]
        # 계약방법
        data_7 = row.find_elements(By.TAG_NAME, "td")[6]
        # 입력일시(+마감일시)
        data_8 = row.find_elements(By.TAG_NAME, "td")[7]

        # 입력일시와 마감일시를 따로 작업.
        # <br>기준으로 나눠서 뽑음
        reg_date = data_8.text.split("\n")[0]
        end_date = data_8.text.split("\n")[1]

        # 입찰공고 상세 주소
        data_link = row.find_element(By.TAG_NAME, "a").get_attribute("href")

        print(
            data_1.text,
            data_2.text,
            data_3.text,
            data_4.text,
            data_5.text,
            data_6.text,
            data_7.text,
            reg_date,  # 이미 텍스트로 뽑아놓음.
            end_date,
            data_link,
        )

        # 엑셀에 저장
        ws.append(
            [
                data_1.text,
                data_2.text,
                data_3.text,
                data_4.text,
                data_5.text,
                data_6.text,
                data_7.text,
                reg_date,
                end_date,
                data_link,
            ]
        )

        time.sleep(2)

# 엑셀 저장
wb.save("./RPAbasic/crawl/download/nara.xlsx")

time.sleep(3)
browser.quit()

print()
