# List Comprehension
# 한줄에 작성

# 리스트 생성 1 ~ 100
numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)


print()

numbers = list(range(1, 101))
print(numbers)


print()


numbers2 = [n for n in range(1, 101)]
print(numbers2)

print()


list1 = ["갑", "을", "병", "정"]
# 정 글자를 제외하고 출력. 지우라는건 아님
for x in list1:
    if x != "정":
        print(x, end=" ")
print()
print([x for x in list1 if x != "정"])


print()
# 1 ~ 100 숫자 중에서 홀수만 출력
list1 = [n for n in range(1, 101) if n % 2 == 1]
print(list1)
print()


print()


# 5글자 이상의 단어만 출력
list2 = ["nice", "study", "python", "anaconda", "abe"]
print([word for word in list2 if len(word) >= 5])
print()

# 소문자만 출력
list3 = ["A", "b", "C", "D", "e", "z"]
for x in list3:
    if x.islower():
        print(x)
print([x for x in list3 if x.islower()])
print()

# 아래 리스트를 각 요소에 *2 한 후 출력
list4 = [1, 2, 3, 4]
print([x * 2 for x in list4])

print([x * 2 for x in range(5)])
print([x * x for x in range(5)])  # 지수의 개념
