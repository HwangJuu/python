# list 구조- 자료형(배열과 같은 개념)
# 대괄호 사용
# 다양한 형태의 자료들을 담을 수 있음.(자바에서는 같은 타입만 담을 수 있음).
# 자료형이 혼합해도 상관없다.

# 생성
list1 = []
list2 = ["a", "b", "c"]
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [1, 2, ["Life", "is", "short"]]  # 2차원 list
list6 = list()

# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)

# print()


# 인덱싱
# print("list2[0] : ", list2[0])
# print("list3[-1] : ", list3[-1])
# print("list4[3] : ", list4[3])
# # 4 + 2 = 6자리 개념이 있음
# print("list4[3] + list5[1] : ", (list4[3] + list5[1]))
# print("list5[2][0] : ", list5[2][0])  # 2번에서 0번을 가지고 나오겠다.
# # ["Life", "is", "short"] 전체가 -1, 안에서 0,1,2,번 이라 short가 출력됨.
# print("list5[-1][2] : ", list5[-1][2])

# print()


# # 슬라이싱 : 어디부터 어디
# print("list2[0:3] : ", list2[0:3])
# print("list3[-1:3] : ", list3[1:3])
# print("list5[2:] : ", list5[2:])


# print()


# list6 = [1, 2, ["a", "b", ["Life", "is"]]]
# # is 출력
# print("list6 [2][2][1] : ", list6[2][2][1])
# print("list6 [-1][-1][1] : ", list6[-1][-1][1])
# print("list6 [2][-1][-1] : ", list6[2][-1][-1])

print()

# 연산자
# + : list와 list의 연결, 숫자와 문자도 가능
# 인덱싱 + : 산술연산자
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]

# print("list1 + list2 = ", (list1 + list2))
# print("list1 + list3 = ", (list1 + list3))
# print("list1[0] + list2[1] = ", (list1[0] + list2[1]))
# 1 + b => TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print("list1[0] + list3[1] = ", (list1[0] + list3[1]))


print()

# * : 반복
# print("list1 * 3 = ", (list1 * 3))  # [1, 2, 3]가 세번 반복됨.
# print("list1[0] *3=", (list1[0] * 3))
# print()

# 리스트 요소 값 변경
# print("list1 = ", list1)
# list1[1] = 7  # 1번 자리에 7 넣기
# print("list1 =", list1)
# list1[2] = "Life"
# print("list1 =", list1)
# print()

# print("list2 =", list2)
# list2[1:2] = [10, 11]
# print("list2 =", list2)
# list2[1] = [15, 16, 17]  # list 안에 list로 삽입
# print("list2 =", list2)
# print()

# 리스트 요소 삭제 : del, []
# print("list1 =", list1)
# del list1[2]
# print("list1 =", list1)
# del list1[1:3]
# print("list1 =", list1)
# list1[1:3] = []
# print("list1 =", list1)
# print()

# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in list1:
#     print(num, end=" ")
# print()

# print()

# # 실습
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# # 리스트 안의 숫자 중 100이상인 숫자 출력
# for num in numbers:
#     if num >= 100:
#         print(num, end=" ")
# print()

# print()
# # 리스트 안의 숫자가 홀수/짝수인지 판별하기
# for num in numbers:
#     if num % 2 == 0:
#         print("{}는 짝수".format(num))
#     else:
#         print("{}는 홀수".format(num))
# print()
# # 리스트 안의 숫자들의 자릿수 출력하기
# # 273 3자리, 103은 3자리, 5는 1자리
# for num in numbers:
#     print("{}은 {}자리".format(num, len(str(num))))
# print()

# 함수
# append() : 리스트에 요소 추가
# list1 = [1, 2, 3]
# # (4,5,6) 형태로 주면 에러남. 여러개를 주고 싶으면 리스트로 묶기
# # TypeError: list.append() takes exactly one argument (3 given)
# list1.append(4)
# list1.append([5, 6, 7])
# print(list1)

# print()

# # 실습 : 1~100까지의 숫자 중에서 짝수 리스트 생성
# even = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         even.append(i)
# print(even)
# print()

# # sort : 오름 차순 정렬(기본) 정렬
# # sort(reverse=True) : 내림차순정렬
# # 숫자
# list1 = [1, 4, 3, 5, 2]
# print("정렬 전 : ", list1)
# list1.sort()
# print("정렬 후 : ", list1)
# print()
# # 영문
# list2 = ["k", "z", "a", "b", "r"]
# print("정렬 전 : ", list2)
# list2.sort()
# print("정렬 후 : ", list2)
# list2.sort(reverse=True)  # 옵션을 이용해 내림차순 출력
# print("내림 차순 정렬 후 : ", list2)
# print()
# # 대소문자 구별 오름차순 A : 65, a : 97에 의해
# list3 = ["k", "z", "K", "b", "A"]
# print("정렬 전 : ", list3)
# list3.sort()
# print("정렬 후 : ", list3)
# print()
# # 한글 정렬도 가능
# list4 = ["ㄷ", "ㄱ", "ㅏ", "ㅂ", "ㅅ"]
# print("정렬 전 : ", list4)
# list4.sort()
# print("정렬 후 : ", list4)
# print()

# reverse() : 리스트 뒤집기
# 정렬이 아니고 거꾸로 출력
# list1 = ["a", "c", "b", "z"]
# list1.reverse()
# print("list1", list1)
# print()

# # sort () + reverse()
list1 = [3, 12, 1, 5, 9, 2, 7]
# print("정렬 전 : ", list1)
# list1.sort()
# list1.reverse()
# print("정렬 후 : ", list1)
# print()

# index() : 위치 반환. 문자열 찾기
# find가 문자열 찾기엔 더 좋음.
print("list1", list1)
print("list1에 9가 있는지 확인", list1.index(9))  # 1로 호출. 1번자리에 있어서
# 값을 못 찾으면 ValueError 발생
# print("list1에 45가 있는지 확인", list1.index(45))  # ValueError: 45 is not in list
print()

# insert(삽입 위치, 삽입할 요소) : 특정 위치에 특정 요소를 삽입할 수 있다.
list1 = [1, 2, 3]
list1.insert(0, 4)  # 0번자리에 4를 삽입. 다른 요소는 뒤로 밀림.
print("list1 요소 삽입 후 : ", list1)
print()

# remove(제거할 요소) : 첫번째로 나오는 요소 삭제. 중복된 요소일 땐 처음 만난 요소 제거
print("list1 요소 제거 전 : ", list1)
list1.remove(2)
print("list1 요소 제거 후 : ", list1)
print()

# pop() : 리스트 요소 꺼내기
# default : 리스트 맨 마지막 요소가 꺼내짐
# pop(위치) : 해당 위치 요소 꺼내기
list1 = [1, 2, 3, 4, 5, 6, 7]
print("list1", list1)
list1.pop()
print("list1 pop() 후 : ", list1)
list1.pop(2)
print("list1 pop(2) 후 : ", list1)
print()

# count(x) : 리스트에 포함된 요소 x의 개수 세기
print("list1.count(2) : ", list1.count(2))  # 2라는 요소가 list1에 몇개 있는지 개수 세어줌.
print()

# extend(x 리스트) : 원래 리스트에 x 리스트 더하기
list2 = [16, 17, 18]
print("list1 + list2 = ", (list1 + list2))
list1.extend(list2)
print("list1 extend(list2) : ", list1)
print()

# clear() : 요소 모두 삭제
list1.clear()
print("list1 clear() 후 : ", list1)
print()

# 요소 in 리스트명 : 리스트 안에 해당 요소가 있는지 확인. True or false로 확인 가능
fruits = ["딸기", "바나나", "수박", "사과", "참외"]
print("딸기" in fruits)
print("두리안" in fruits)
print()

# 리스트가 비어 있으면 거짓
list1 = []
if list1:
    print("참")
else:
    print("거짓")


print()

# 리스트 요소 출력
# for num in enumerate(numbers):
#     print(num)  # (0, 273) : (인덱스, 값) ==> 튜플 자료형 형태로 반환
# print()

# (variable) idx: int
# idx, num = (0,273)
# for idx, num in enumerate(numbers):
#     # print(num)
#     print(idx, num)

print()

# enumerate() : 하나씩 가지고 나올 수 있는 자료형에 사용가능
for idx, num in enumerate(numbers, start=1):
    print(idx, num)
print()

# 실습
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다
# 70, 66, 55, 75, 90, 95, 80, 85, 100, 87
# 중간고사 점수를 리스트로 생성하고 A학급의 평균을 구하시오.
A_class = [70, 66, 55, 75, 90, 95, 80, 85, 100, 87]
total = 0
for num in A_class:
    total += num
print("A학급의 평균 : %.2f " % (total / len(A_class)))
# for 사용 안하고
print("A학급의 평균 : %.2f " % (sum(A_class) / len(A_class)))


print()
# 다음 리스트에서 Apple 항목만 삭제하고 출력하기
# ["Banana","Apple", "Orange","Grape"]
fruits = ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple")
print(fruits)

print()
