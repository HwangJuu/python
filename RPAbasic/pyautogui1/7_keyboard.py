print()
# 키보드 자동화
import pyautogui as p

# 입력 : write()
# p.write("write")

# 메모장에 문자열 타이핑
# 화면에 메모장이 안보여도 가능. 띄어만 놓기
# 현재 화면에 메모장 활성화
notepad = p.getWindowsWithTitle("제목 없음")[0]
notepad.activate()
# p.write("write")
# p.write("pyautogui", interval=0.5)
# p.write("안녕하세요")  # 한글 지원 안함

# # 해야 할 작업을 리스트로 작성
# p.write(
#     ["h", "e", "l", "l", "o", "left", "left", "right", "l", "o", "enter"],
#     interval=0.25,
# )


# hotkey(조합키)
# import pyperclip  # 클립보드 이용하는 개념
# # 클립보드 복사해서 붙여넣기

# pyperclip.copy("안녕하세요")  # ctrl + c
# p.hotkey("ctrl", "v")
# p.hotkey("ctrl", "a")
# # 작업관리자 단축키
# p.hotkey("ctrl", "shift", "esc")


# keyDown() +  keyUp() == press()
# p.keyDown("shift")
# p.press("4")
# p.keyUp()

# 2번 작성
p.press(["a", "b", "c"], 2)
# 2번 작성 1초뒤에
p.press(["#", "$", "%"], 2, 1)

print()
