print()
# 병합정렬 : 분해 + 병합


def merge_sort1(list1):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료 조건 : 분해, 병합을 안해도 되는 상황
    if size <= 1:  # 하나만 있으면 정렬할 필요 없음
        return list1

    # 분해 작업
    mid = size // 2  # 중간 구하기(정수나눗셈)

    #
    # 재귀호출로 첫번째 그룹[6, 8, 3, 9, 10] => mid=2 g1 = [6,8], g2 = [3,9,10] .. => 하나가 남을 때까지 계속 루프
    g1 = merge_sort1(list1[:mid])

    # 재귀호출로 두번째 그룹[1, 2, 4, 7, 5] => mid=2 g1 = [1,2], g2 = [4,7,5] ..=> 하나가 남을 때까지 계속 루프
    g2 = merge_sort1(list1[mid:])

    # 병합 작업
    # python은 리스트가 비어 있으면 False로 인식.
    result = []

    # len(g1) > 0 and
    while g1 and g2:  # 두 그룹에 자료 남아 있으면
        # 하나씩 비교
        # 비어있는 리스트에 더 작은 값 넣기.
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 자료 비교 후 남아있는 요소 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print("병합 정렬 : ", merge_sort1(list1))

# 구문 이해가 되지 않을시 중간중간  print() 구문을 넣어 직접 눈으로 확인하기.


print()
