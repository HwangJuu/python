print()
# 숫자 n개를 리스트에 입력받아 최솟값 구하기

# 숫자 입력 받은 후 list1에 추가
# q라는 문자가 입력되면 리스트 추가하는걸 종료
def num_input(list1):

    i = 1

    print("리스트에 추가할 숫자를 입력하세요\n 숫자 추가를 끝내기 위해서는 q를 입력하세요")
    while True:
        print(str(i), ": ", end="")
        num = input()

        if num != "q":
            list1.append(int(num))
        else:
            break
        i = i + 1


# 최소값 구하기
def find_min(list1):
    # 리스트 첫번째 요소 max에 담기
    min = list1[0]
    size = len(list1)

    for i in range(1, size):
        if min > list1[i]:
            min = list1[i]
    # for문이 끝난 후에 min값을 돌려주면 됨
    return min


if __name__ == "__main__":
    list1 = list()  # 비어있는 리스트 생성
    num_input(list1)
    print("최소값 : ", find_min(list1))


print()
