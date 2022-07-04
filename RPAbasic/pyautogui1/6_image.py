print()
# 이미지 인식
import pyautogui as p

# locateOnScreen(path, confidence) : 캡쳐한 이미지의 화면상 좌표 구하기
# confidence : 신뢰도(default 1, 0.8~0.9로 설정) - opencv-python 라이브러리 설치
# 이미지 기반이어서 해상도가 바뀐다거나 이런 경우는 잘 안됨
# 이미지 파일명은 영문으로 작성

# 화면상 보여야지 값이 나옴
# 제일 뒤에 있으면 None으로 나옴
# screen_locate = p.locateOnScreen("./RPAbasic/pyautogui1/screen.png")
# print(screen_locate)  # Box(left=1203, top=441, width=300, height=400)

# screen_locate = p.locateOnScreen("./RPAbasic/pyautogui1/file_menu.png", confidence=0.9)
# print(screen_locate)
# p.click(screen_locate)

# locateAllOnScreen() : 찾아야 하는 이미지가 여러개 있는 경우
# p.sleep(2)
# for i in p.locateAllOnScreen("./RPAbasic/pyautogui1/checkbox.png", confidence=0.9):
#     print(i)
#     p.click(i)

# 찾아야 하는 대상이 화면에 늦게 나타나는 경우
# 1) 찾을때까지 반복시키기
file_menu = p.locateOnScreen("./RPAbasic/pyautogui1/checkbox.png", confidence=0.9)
# file_menu가 없다면 계속 찾아줘
while file_menu is None:
    file_menu = p.locateOnScreen("./RPAbasic/pyautogui1/checkbox.png", confidence=0.9)
    print("발견할 수 없음")

# 계속 찾다가 발견하면 클릭
p.click(file_menu)

# 2) 일정한 시간만큼만 기다리기
import time, sys

# 기다리는 시간 지정
timeout = 15

# 시작 시간
start = time.time()
file_menu = p.locateOnScreen("./RPAbasic/pyautogui1/checkbox.png", confidence=0.9)
# file_menu가 없다면 계속 찾아줘
while file_menu is None:
    file_menu = p.locateOnScreen("./RPAbasic/pyautogui1/checkbox.png", confidence=0.9)

    end = time.time()

    if end - start > timeout:
        print("시간종료")
        sys.exit()

# 계속 찾다가 발견하면 클릭
p.click(file_menu)

print()
