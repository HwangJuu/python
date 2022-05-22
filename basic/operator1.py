# 연산자
# 산술 연산자 : +,-,*,/(실수),//(정수),%,**

a,b = 5,3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

print()
s1, s2, s3 = "100","100.123","999999999"
print(s1+s2+s3) # + : 연결 => 100100.123999999999 문자로 인식
print(float(s1) +float(s2)+float(s3)) # 형변환 후 연산
# str + int는 안해줌
#print(s1+1) =>TypeError: can only concatenate str (not "int") to str 
print(int(s1)+1)

# 복합대입연산자 : +=, -+, *=, /=, //=, %=,**=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5 
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)

print()
# 실습 : 777,777원
# 화폐교환 : 5만원/1만원/5천원/1천원
money = 777777
m50000 = money // 50000
money %= 50000

m10000 = money // 10000
money %= 10000

m5000 = money // 5000
money %= 5000

m1000 = money // 1000
money %= 1000

print("50,000원 : %d 장" % m50000)
print("10,000원 : %d 장" % m10000)
print("5,000원 : %d 장" % m5000)
print("1,000원 : %d 장" % m1000)
print("나머지 돈 : %d" % money)

#관계연산자 : ==, != >,<, >=,<=
a,b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

#논리연산자 : and, or, not 기호 사용 불가
print(100 > 60 and  60 > 15)
#print(100 > 60 &&  60 > 15)
print(100 > 60 or  60 < 15)
print(not 60 < 15)
print(not False)
print(not True)
#print(!True)

#비트연산자
print(10 & 7) # 2
print(10 | 7) # 15
print((100> 60) & (60 > 15)) # True & True => True
