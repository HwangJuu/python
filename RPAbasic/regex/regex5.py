print()
# data_kr.xlsx 파일읽기

import re
from openpyxl import load_workbook

# 원본 문자 : python VS java
# VS를 기준으로 문자열 분리 => ['python', 'java']
pattern = re.compile(" VS ")  # 공백까지 확인
print(pattern.split("python VS java"))
print()
# 주민번호 컬럼을 읽어서 화면 출력 단, 주민번호 뒷자리는 *로 변경해서 출력
wb = load_workbook("./RPAbasic/crawl/download/data_kr.xlsx")
ws = wb.active

for each_row in ws.rows:
    print(each_row[1].value)  # 값 출력 확인

# 찾아야하는 패턴 : 주민등록번호 뒷자리
pattern = re.compile("[0-9]{7}")  # 0~9사이의 7개가 와야함.
for each_row in ws.rows:
    print(re.sub(pattern, "*******", each_row[1].value))

wb.close()  # 엑셀 닫기

print()
