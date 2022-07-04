print()
# 최대수익 (== 최대값, 최소값이 아님)
# 입력 : 주식 가격 변화 리스트
# 출력 : 한 주를 사고 팔아 얻을 수 있는 최대 수익

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


if __name__ == "__main__":
    # 날짜별 매매가 나열
    stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
    print("최대수익", max_profit(stock))

print()
