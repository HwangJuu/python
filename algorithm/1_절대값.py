print()
# 절대값

# a의 절대값 구하기
# 1) 부호 판단
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


import math

# 2) 제곱 후 제곱근
def abs_sign2(a):
    b = a * a
    return math.sqrt(b)  # sqrt 소수점으로 출력


# 모듈로 보고 실행
if __name__ == "__main__":
    print("절대값", abs_sign(5))
    print("절대값", abs_sign(-3))
    print()
    print("절대값", abs_sign2(5))
    print("절대값", abs_sign2(-3))

print()
