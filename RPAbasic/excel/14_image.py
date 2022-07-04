print()
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

# ImportError: You must install Pillow to fetch image objects
# 추가 라이브러리 필요 : pip install Pillow
img = Image("./RPAbasic/excel/dog.jpg")

ws.add_image(img, "C3")
wb.save("./RPAbasic/excel/image.xlsx")


print()
