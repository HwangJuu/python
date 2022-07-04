# set : 집합자료형
# 자바의 Set 과 같은 개념
# 중복 허용 안됨
# 순서 없음.(order by가 없음). 인덱싱, 슬라이싱 사용할 수 없음

set1 = set()
set2 = set("Hello")
set3 = set([1, 2, 3, 4])
set4 = set([1, 2, 3, 4, 6, 6])
set5 = set({"no": "1", "name": "hong", "age": 24})

print()
print(set1)
print(set2)  # 중복된 문자는 하나만 출력.
print(set3)
print(set4)
print(set5)  # 키 값을 기반으로 해서 출력
print()

# set ==> tuple 변환
print(tuple(set3))

# set ==> list 변환
print(list(set3))
print()

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("s1, s2 교집합", s1 & s2)
print("s1, s2 교집합", s1.intersection(s2))
print()
print("s1, s2 합집합", s1 | s2)
print("s1, s2 합집합", s1.union(s2))
print()
print("s1, s2 차집합", s1 - s2)
print("s1, s2 차집합", s1.difference(s2))
print()

# 함수
# add() : 값 하나 추가
print(s1)
s1.add(17)
print(s1)
print()

# update() : 여럭 개의 값을 한꺼번에 추가
s1.update([18, 19, 20])
print(s1)
print()

# remove() : 특정 값 제거
s1.remove(2)
print(s1)
print()
