print()
# 최대공약수 - 유클리드 호제
# 규칙 1) a와 b의 최대공약수는 b와 a를 b 로 나눈 나머지의 최대공약수와 같다
#          gcd(a,b) == gcd(b, a%b)
# 규칙 2) 어떤 수와 0의 최대 공약수는 자기 자신

# gcd(60,24) = gcd(24,60%24) = gcd(24, 12) = gcd(12, 24%12) = gcd(12,0) = 12


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print("유클리드 호제 1과 5 최대공약수 : ", gcd(1, 5))
    print("유클리드 호제 1과 5 최대공약수 : ", gcd(3, 6))
    print("유클리드 호제 1과 5 최대공약수 : ", gcd(60, 24))
    print("유클리드 호제 1과 5 최대공약수 : ", gcd(81, 27))

print()
