print()
# 사용자가 정의한 모듈 실습

# import prints

# prints.prt1()
# prints.prt2()


import mod1

# print(mod1.sum(15, 25))
# print(mod1.safe_sum(15, "25"))
# mod1.py 에 return 값이 없으면 None으로 출력

# from prints import prt1

# prt1()

# from mod1 import sum

# print(sum(45, 25))

# import calc

# num1, num2 = 10, 5
# four1 = calc.FourCal(num1, num2)
# print("{} + {} = {}".format(num1, num2, four1.add()))
# print("{} - {} = {}".format(num1, num2, four1.sub()))
# print("{} * {} = {}".format(num1, num2, four1.mul()))
# print("{} / {} = {}".format(num1, num2, four1.div()))


from calc import FourCal

num1, num2 = 10, 5
# four1 = calc.FourCal(num1, num2)
four1 = FourCal(num1, num2)
print("{} + {} = {}".format(num1, num2, four1.add()))
print("{} - {} = {}".format(num1, num2, four1.sub()))
print("{} * {} = {}".format(num1, num2, four1.mul()))
print("{} / {} = {}".format(num1, num2, four1.div()))

print()
