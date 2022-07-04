print()
# 정규 표현식
# 특정한 패턴과 일치하는 문자열을 검색, 치환, 제거하는 기능

# 정규표현식 생성 - re 모듈
# 메소드
# 1) match() : 문자열 처음부터 정규식과 매칭되는 패턴 찾아서 리턴
# 2) search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴 찾아서 리턴
# 3) findall() : 정규식과 일치하는 모든 문자열을 찾아 리스트로 반환
# 4) finditer() : 정규식과 일치하는 모든 문자열을 찾아 iterator 객체로 반환

import re

# 패턴 생성
pattern = re.compile("D.A")  # 가지고 있는 문자열에 "D.A"이 있는지 찾고 싶음
# . : 어떤 문자와도 매칭됨.

# 패턴 매칭 여부 확인
result = pattern.search("DAA")
print(result)  # <re.Match object; span=(0, 3), match='DAA'>
# 돌아오는 형태는 Match 형태
print("패턴 시작 위치", result.start())  # 시작 위치
print("패턴 끝 위치", result.end())
print("패턴과 일치하는 문자열", result.group())
print("패턴과 일치하는 위치", result.span())  # 튜플로 묶어서 받을 수 있음

print()

result = pattern.search("D1A")
print(result)

print()

result = pattern.search("D00A")
print(result)  # 매칭 되지 않으면 None으로 돌아옴

print()

result = pattern.search("d0A D2A 0111")
print(result)

print()

# re.compile() 사용하지 않고 간단하게 만들기
print(re.search(r"D.A", "DAA"))  # 패턴이 없기 때문에 re를 사용
print(re.search(r"D.A", "D1A"))
print(re.search(r"D.A", "D00A"))

print()
