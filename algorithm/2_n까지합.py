print()
# 1~10까지의 합 : 55
# 1~100 까지 합 : 5050

# 1) 반복문
def sum_a(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


# 2) n(n+1)/2
def sum_a2(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    print("1~10 합 : ", sum_a(10))
    print("1~100 합 : ", sum_a(100))
    print()
    print("1~10 합 : ", sum_a2(10))
    print("1~100 합 : ", sum_a2(100))


print()
