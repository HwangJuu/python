print()
# 셀 이동
from openpyxl import load_workbook


wb = load_workbook("./RPAbasic/excel/range.xlsx")
ws = wb.active

# 이동시킬 범위잡기
# move_range(cell_range, rows, cols)
# rows는 그대로 두고, cols는 오른쪽 옆으로 한칸
# - 를 주게 되면 왼쪽/ 위로 이동
ws.move_range("B1:C11", rows=0, cols=1)


wb.save("./RPAbasic/excel/range_move.xlsx")


print()
