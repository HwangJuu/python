print()
# match 사용

import re

pattern = re.compile("[a-z]+")  # 소문자만 나와야하고(최소 1~ 최대 무한대)

matched = pattern.match("Dave")
print("match()", matched)  # 처음부터 매치가 안되서 안찾음

searched = pattern.search("Dave")
print("search()", searched)  # 전체 조회해서 같으면 출력

print()
# re.sub(패턴, 바꿀문자열, 원본문자열) : 찾아서 바꾸기
ori_text = "DDA D1A DDDA DA"
print("re.sub : ", re.sub("D.A", "Dave", ori_text))

print()
# findall() : 정규식과 일치하는 모든 문자열을 찾아 리스트로 반환
print("findall : ", pattern.findall("Game of Life in Python"))
pattern = re.compile("[a-zA-Z]+")
print("re.sub findall : ", pattern.findall("Game of Life in Python"))

print()
# finditer() : 정규식과 일치하는 모든 문자열을 찾아 iterator 객체로 반환
for m in pattern.finditer("Game of Life in Python"):
    print(m)  # match 형태
    print("finditer : ", m.group())

print()
# split() : 정규식을 기준으로 문자열 분리 후 리스트로 반환
pattern = re.compile(":")
print("split : ", pattern.split("python:java"))

print()
