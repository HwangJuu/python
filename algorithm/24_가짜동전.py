print()
# 가짜 동전 찾기
# 주어진 동전 n개 중에서 가짜 동전 찾기
# 입력 : 전체 동전 위치의 시작과 끝
# 출력 : 가짜 동전의 위치 번호

# 양팔 저울
# 두개의 그룹
# a ~ b까지 동전
# c ~ d까지 동전

# a ~ b에 가짜 동전이 있다면 -1 리턴
# c ~ d에 가짜 동전이 있다면 1 리턴
# 가짜 동전이 없다면 0 리턴

# for문으로 weight을 계속 돌려야함.
def weight(a, b, c, d):
    # 임의의 fake 동전 위치
    fake = 29
    if a <= fake and fake <= b:  # a <= fake <= b
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fakecoin(left, right):

    # 종료 조건
    if left == right:
        return left

    half = (right - left + 1) // 2  # 반나눠서 두그룹 생성

    # 100개의 동전이 있다고 할 때 0~ 49 가 g1,
    # 50 ~ 99가 g2
    # 왼쪽 그룹 g1
    g1_left = left
    g1_right = left + half - 1
    # 오른쪽 그룹 g2
    g2_left = left + half
    g2_right = g2_left + half - 1

    # result == -1 or 0 or 1
    result = weight(g1_left, g1_right, g2_left, g2_right)

    if result == -1:  # 그룹1에 가짜 동전 있음. g1 그룹에서 또 나누기
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:  # 그룹 2에 가짜 동전 있음. g2 그룹에서 또 나누기
        return find_fakecoin(g2_left, g2_right)
    else:  # 두 그룹에 가짜 동전 없음
        return right  # 두 그룹으로 나뉘지 않고 남은 나머지 한개의 동전이 가짜


if __name__ == "__main__":
    n = 100
    print("가짜 동전 위치 : ", find_fakecoin(0, n - 1))


print()
