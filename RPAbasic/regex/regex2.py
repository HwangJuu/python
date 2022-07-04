print()
import re

pattern = re.compile("D?A")

print("? : 최소 0 ~ 최대 1")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))

print()
pattern = re.compile("D*A")

print("* : 최소 0 ~ 최대 무한대")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDA"))

print()
pattern = re.compile("D+A")

print("+ : 최소 1 ~ 최대 무한대")
print(pattern.search("A"))  # None
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDA"))

print()
pattern = re.compile("AD{2}A")

print("{n} : n만큼 반복")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # 패턴만큼 출력
print(pattern.search("ADDDDDDDDDDA"))  # 2개 이상이니 None

print()
pattern = re.compile("AD{2,6}A")

print("{n,m} : 최소 n, 최대 m")
print(pattern.search("ADA"))  # 범위내에 만족하지 못함
print(pattern.search("ADDA"))  # 최소 2개에 조건 만족
print(pattern.search("ADDDDDDA"))  # 최대 6개 조건 만족

print()
