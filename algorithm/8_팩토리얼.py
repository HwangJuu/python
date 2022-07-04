print()
# 팩토리얼
# 4! = 4 * 3 * 2 * 1


def fact(n):
    result = 1
    # range사용하면 마지막 번호를 사용하지 않는데 사용해야하기 때문에 +1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == "__main__":
    print("3! = ", fact(3))
    print("5! = ", fact(5))
    print("10! = ", fact(10))

print()
