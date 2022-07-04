print()
# 최대수익 (== 최대값, 최소값이 아님)
# 입력 : 주식 가격 변화 리스트
# 출력 : 한 주를 사고 팔아 얻을 수 있는 최대 수익
# 시간측정
import random
import time

# 하나하나 비교
def max_profit(stock):
    size = len(stock)
    max_profit = 0

    # 현재 기준 날짜로 전날짜는 판매 못함. 다음날만 판매 가능
    for i in range(size - 1):
        for j in range(i + 1, size):
            profit = stock[j] - stock[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


# 파는 날을 기준으로 최소값 찾기 앞쪽에 날짜에서 비교
def max_profit2(stock):
    size = len(stock)
    max_profit = 0

    # 첫째 날의 주가를 최솟값으로 시작
    min_price = stock[0]

    for i in range(1, size):
        profit = stock[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if stock[i] < min_price:
            min_price = stock[i]

    return max_profit


# 시간 측정
def test(n):
    # 주가에 해당하는 숫자 랜덤 생성
    stock = []
    for i in range(0, n):
        stock.append(random.randint(5000, 20000))

    # O(n*n) 알고리즘
    start = time.time()
    mps = max_profit(stock)
    end = time.time()
    time_slow = end - start

    # O() 알고리즘
    start = time.time()
    mpf = max_profit2(stock)
    end = time.time()
    time_fast = end - start

    # 입력크기, 각각 알고리즘이 계산한 최대 수익
    print("크기", "최대수익", "최대수익")
    print(n, mps, mpf)

    diff = 0
    if time_fast > 0:
        diff = time_slow / time_fast

    # 시간 얼마나 걸리는지
    print("%d %.5f % .5f %.2f" % (n, time_slow, time_fast, diff))
    print()


if __name__ == "__main__":
    test(100)
    test(10000)

print()
