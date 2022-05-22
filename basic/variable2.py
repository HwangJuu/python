# 변수 - 타입이 없음(값을 할당하면 타입이 생김)
# str, int, float, bool

#문자형 - "" , '' 둘다 허용
str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """
Life is too short, You need Python
"""
str4 = '''
Life is too short, You need Python
'''
str5 = "Python's favorite food"
print(str1)
print(str2)
print(str3)
print(str4)

# 문자열 연산
head = "Python"
tail = " is fun"
# + : 문자열 연결
print(head + tail)

# * : 반복
a = "python"
print(a * 2)

print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱 
str1 = "Life is too short"
# 왼쪽을 기준으로 0
print("str1[3]", str1[3]) #e
# 오른쪽을 기준으로 -1
print("str1[-3]", str1[-3]) #o
print()
#범위지정 가능
# 마지막 숫자 범위는 포함 안함
print("str1[0:4]",str1[0:4]) # Life
# 공백 포함해서 
print("str1[4:8]",str1[4:8]) # is
#9부터 시작해서 끝까지
print("str1[9:]",str1[9:]) #oo short
print("str1[:17]",str1[:17]) #Life is too short
print("str1[0:-4]",str1[0:-4]) #Life is too s

#실습
str2 = "20220520Sunny"
#date 변수에 날짜만 담기
date = str2[0:8]
print(date)
#weather 변수에 날씨만 담기
weather = str2[8:]
print(weather)

#date 변수에 있는 값을 2022-05-20 출력
year = date[0:4]
month = date[4:6]
day = date[6:]
print(year,month,day, sep="-")
#date, weather 출력 2022-05-20 Sunny출력
print(year,month,day, sep="-", end=" ")
print(weather)

# 문자열 관련 함수들
# len()
print("문자열 길이", len(str1))
# count()
print("문자열에 포함된 특정 문자의 수", str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : %d" % str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : {}".format(str1.count('t')))
#find()
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i"))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("k"))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i",4))
# index() : 찾는 문자열이 없다면 에러 발생
print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("i"))
# 에러가 나면 그 뒤부터는 실행이 안되기 때문에 막아야함.
# print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("k")) # ValueError: substring not found
print()
#startswith() : ~시작하는 문자. boolean 타입, 대소문자 구분
print(str1.startswith("L")) #True
print(str1.startswith("l")) #False
# endswith() : ~ 끝나는 문자
print(str1.endswith("t")) #True
print(str1.endswith("T")) #False
print()
# join() : 삽입
a = ","
print(a.join("abcde"))
# upper / lower : 대소문자 변경
a = "abcde"
print("소문자를 대문자로 변경", a.upper())
a = "ABCDE"
print("대문자를 소문자로 변경", a.lower())
# swapcase() : 대소문자를 상호 변환
a = "Python is Easy"
print(a.swapcase())
# title() : 첫글자만 대문자
print("python Is Easy".title())

print("abc"=="ABC")
print()
# 공백제거 : strip(), lstrip(), rstrip()
a = "        hi        "
print(a.lstrip()) # 왼쪽 공백 제거
print(a.strip()) # 양쪽 공백 제거
print(a.rstrip()) #오른쪽 공백 제거
print()
# replace() : 문자열 바꾸기
print(str1.replace("Life", "Your leg"))
print()
# split() : 문자열 나누기. 리스트 구조로 리턴(자바에선 배열). default:공백을 기준으로 나눠줌
print(str1.split()) #['Life', 'is', 'too', 'short']
a = "a:b:c:d"
print(a.split(":")) #['a', 'b', 'c', 'd'] : 콜론을 기준으로 
# splitlines() : 줄바꿈(엔터)을 기준으로 나누기
print(str1.splitlines())
a = "하나\n둘\n셋"
print(a.splitlines()) #['하나', '둘', '셋']

#문자열 구성 파악
print("1234".isdecimal())
print('abcd'.isalpha())
print('abc123'.isalnum())
print("abcd".islower())
print("ABCD".isupper())

#실습 : 암호 생성
# http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 . 이후 부분은 제외 =>naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 개수 + ! 로 구성 => nav51!
# 결과 : nav51!
url = "http://naver.com"
url = url.replace("http://","") #규칙1
print(url)
url = url[:url.find(".")] #규칙2 0:5
print(url)
e_cnt = url.count("e") #글자 내 e 문자 개수

# 타입에러 url[:3] => 문자, len(url)=> 숫자, e_cnt=> 숫자, ! => 문자
# 문자 + 숫자 : 연결 되지 않고 에러 발생
#password = url[:3] + len(url)+ e_cnt+"!" #규칙 3 => TypeError: can only concatenate str (not "int") to str
# 문자 + str(숫자) : 연결
password = url[:3] + str(len(url))+ str(e_cnt)+"!"  #규칙3  str(숫자) => 문자로 인식
print(password)

