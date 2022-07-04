print()
# 동명이인 찾기
# ["Tom","Jerry","Mike","Tom"]

# Tom 입장 : 3번 비교 == (n-1)
# Jerry 입장 : 2번 비교 == (n-2)
# Mike 입장 : 1번 비교 == (n-3)
# Tom 입장 : 0번 비교 == (n-n)

# 계산 복잡도 O(n제곱)

# 중복된 이름을 set() 에 추가한 후 리턴
def dup_name(list1):
    result = set()
    size = len(list1)

    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if list1[i] == list1[j]:
                result.add(list1[i])
    return result


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike", "Tom"]
    print(dup_name(list1))

print()
