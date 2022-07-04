print()
from openpyxl import load_workbook

wb = load_workbook("./RPAbasic/excel/range.xlsx")
ws = wb.active

# 행 삽입
ws.insert_rows(8)

# 8번 위치부터 5행 삽입
ws.insert_rows(8, 5)

# 열 삽입
ws.insert_cols(2)
# 2번 컬럼부터 3개
ws.insert_cols(2, 3)


wb.save("./RPAbasic/excel/range.xlsx")

print()
