print()
import pyautogui as p

# # getActivWindow() : 현재 활성화된 창 가지고 오기
# w = p.getActiveWindow()
# print(w)
# print(w.title)
# print(w.size)
# print(w.left, w.right, w.top, w.bottom)
# p.click(w.left + 25, w.top + 20)

# getAllWindows() : 현재 윈도우에 떠 있는 모든 창 가져오기
for w in p.getAllWindows():
    print(w)

# # getWindowsWithTitle() : 특정 타이틀을 가진 창 모두 가져오기
# w = p.getWindowsWithTitle("제목 없음")[0]
# # 활성화 된 상태가 아니라면 활성화시키기
# if not w.isActive:
#     w.activate()

# # 최대화가 아니라면 최대화 시키기
# if not w.isMaximized:
#     w.maximize()

# p.sleep(1)

# # 최소화 상태가 아니라면
# if not w.isMinimized:
#     w.minimize()

# # 창 종료
# p.sleep(1)
# w.close()  # 프로그램 종료. 메모장에 내용이 있다면 저장 여부 확인.

print()
