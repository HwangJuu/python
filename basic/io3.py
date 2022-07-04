print()
# csv 파일 입출력
import csv

# with open("data/sample1.csv", "r") as f:
#     # csv 행단위로 읽어옴.
#     reader = csv.reader(f)  # reader 읽어오기

#     # 헤더명 제거
#     # next(reader)  # ['번호', '이름', '가입일시', '나이'] 안나오게

#     print(reader)  # <_csv.reader object at 0x000002CE0C3C1720>
#     print(type(reader))
#     print(dir(reader))
#     print()
#     for c in reader:
#         print(c)


# sample2 읽어오기

# with open("data/sample2.csv", "r") as f:

#     reader = csv.reader(f)
#     # 옵션 추가 구별해줄 구문을 넣으줌
#     reader = csv.reader(f, delimiter="|")

#     for c in reader:
#         print(c)  # 줄 단위로 읽어옴

# csv ==> dict 형태로 읽어오기
# with open("data/sample1.csv", "r") as f:
#     reader = csv.DictReader(f)

#     for c in reader:
#         print(c)  # {'번호': '9', '이름': '김은미', '가입일시': '2017-02-08 07:44:33', '나이': '51'}
#         for k, v in c.items():
#             print(k, v)
#         print()


# sample3 읽기 숫자만 들어있음.
# with open("data/sample3.csv", "r") as f:
#     reader = csv.DictReader(f)
#     reader = csv.reader(f)  # 리스트 형태로 읽어옴

#     for c in reader:
#         print(c)

# # csv 파일 만들기
# # 1차원 리스트 csv파일로 저장
# list1 = [1, 2, 3, 4, 5]  # list1 = list(range(1,6))

# with open("data/sample4.csv", "w") as f:
#     wt = csv.writer(f)

#     wt.writerow(list1)  # 줄(행) 단위 적겠다

# 2차원 리스트
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open("data/sample5.csv", "w", newline="") as f:

    wt = csv.writer(f)

    # for문을 사용시 조건을 넣을 수 있음
    # for row in list1:
    #     wt.writerow(row)  # 한줄한줄 확인하면서 입력 가능

    # writerrows 한번에 다 입력하겠다.
    wt.writerows(list1)


print()
