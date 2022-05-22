# for문
# for 변수 in 범위:

# 범위에 해당하는 부분을 리스트로 만들어줌. 시작 값을 안주면 0
# range(시작값, 마지막범위, 증감)
# print(range(5)) # 시작은 0부터 
# print(list(range(5)))
# print(list(range(1,5)))
# print(list(range(0,10,2))) # 0부터 시작해서 10까지, 2씩 증가
# print(list(range(50,1,-2))) # 50부터 시작해서 1까지, -2씩 감소

# 0~9 출력
from cgi import print_arguments


for i in range(10):
    print(i, end=" ")
print()

for i in range(1,11):
    print(i, end=" ")
print()

# 1~100출력
for i in range(1,101):
    print(i, end=" ")
print()

# 1~100 홀수 출력
for i in range(1,101,2):
    print(i, end=" ")
print()

# 1~ 100 합계 
sum1 = 0
for i in range(1,101):
    sum1 += i
print("1~ 100 합계 : ",sum1)
print()

# 실습
# 사용자한테 숫자를 입력받은 후 1 ~ 사용자 입력값까지 합계를 구한 후 출력
# num = int(input("숫자 입력 : ")) +1
# sum1 = 0
# for i in range(1,num):
#     sum1 += i
# print("입력한 숫자까지의 합 :", sum1)
# print("1 ~ {} 까지 합 : {} ".format(num, sum(range(1,num))))

# 문자열 출력
word = "dreams"
for s in word:
    print(s)

# 이중 for문
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# 구구단 2~9eks
# 2*1 = 2 ~~~
# 3*1 = 3 ~~~
for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,(i*j)), end="\t")
    print()

# break, continue
i = 1
while i<=10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
print()

i = 1
while i<=10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")
print()
   
# 실습 : 1 ~ 10 출력, i 가 5인 경우는 출력하지 않음
# for + continue
for i in range(1,11):
    if i == 5:
        continue
    print(i, end=" ")
print()