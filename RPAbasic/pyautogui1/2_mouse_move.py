print()
import pyautogui

# 좌표인식 - position()
# pos = pyautogui.position()
# print(pos)
# print(pos.x, ", ", pos.y)

# 마우스 이동 - moveTo(x,y,시간) : 절대좌표
# 어디로 갈껀지
# duration=1 1초동안 움직이기
# pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=1)


# 마우스 이동 - moveRel(x,y,시간) / move(x,y,시간) : 상대좌표
pyautogui.moveTo(300, 300, duration=1)
pyautogui.moveRel(100, 100, duration=0.5)
print(pyautogui.position())


print()
