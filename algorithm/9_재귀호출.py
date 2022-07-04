print()
# 재귀호출 : 함수 안에서 자기 자신을 부르는 것

# # 잘못된 예제
# def hello():
#     print("hello")
#     hello()


# hello()
# # RecursionError: maximum recursion depth exceeded while calling a Python object : 데이터를 많이 사용하니 자동으로 멈춤

# 팩토리얼
def fact(n):
    # 기본 단계 - 끝내는 부분
    if n == 1:
        return 1
    # 반복단계
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    print("3! = ", fact(3))
    print("5! = ", fact(5))
    print("10! = ", fact(10))
    print()

# n까지의 합
def rec_sum(n):
    if n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)  # n * (n + 1) // 2


if __name__ == "__main__":
    print("3까지의 합 = ", rec_sum(3))
    print("5까지의 합 = ", rec_sum(5))
    print("10까지의 합 = ", rec_sum(10))


print()
