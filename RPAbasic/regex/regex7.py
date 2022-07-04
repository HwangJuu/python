print()
# train.xlsx 읽어서 정규식 적용

from openpyxl import load_workbook
import re

path = "./RPAbasic/crawl/download/"
wb = load_workbook(path + "train.xlsx")
ws = wb.active

# Name 출력 : 4번째 행.
for each_row in ws.rows:
    print(each_row[3].value)

# 전체 성별을 가지고 올때
pattern = re.compile(" [A-Za-z]+\.")

# Name 출력 : Braund, Mr. Owen Harris ==> Mr.부분 찾는 패턴
for each_row in ws.rows:
    print(each_row[3].value)
    print(pattern.findall(each_row[3].value))
    # print(
    #     pattern.search(each_row[3].value).group()
    # )  # AttributeError: 'NoneType' object has no attribute 'group'

# 남자만 알고 싶을때
pattern = re.compile(" Mr\.")

for each_row in ws.rows:
    # print(each_row[3].value)
    # print(pattern.findall(each_row[3].value))  # 찾은게 없다면 빈 괄호
    if len(pattern.findall(each_row[3].value)) > 0:
        print(each_row[3].value)

wb.close()


print()
