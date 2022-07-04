print()
# 하나가지고 정렬하기


def quick_sort(list1, start, end):

    # 종료
    # 하나의 리스트가 0이면 더이상 할 필요 없음
    if end - start <= 0:
        return

    # 기준값 정하기
    pivot = list1[end]

    i = start

    # 정렬할 땐 for문 사용
    for j in range(start, end):
        if list1[j] < pivot:
            list1[i], list1[j] = list1[j], list1[i]
            i += 1

    list1[i], list1[end] = list1[end], list1[i]

    # 재귀호출
    quick_sort(list1, start, i - 1)
    quick_sort(list1, i + 1, end)


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    # start값 = 0, end값 = len(list1)-1
    quick_sort(list1, 0, len(list1) - 1)
    print("퀵정렬 : ", list1)


print()
