print()
# json 읽고 쓰기

import json

# json 읽기
data = '{"id": "hong", "language": "python", "edition": "3.9", "author": "Guido van Rossum"}'

# 문자열 형태를 json 로드
# json_data = json.loads(data)

# # print(type(json_data))  # <class 'dict'>
# print(
#     type(json_data),
#     json_data["id"],
#     json_data["language"],
#     json_data["edition"],
#     json_data["author"],
# )

data = {
    "id": "hong",
    "language": "python",
    "edition": "3.9",
    "author": "Guido van Rossum",
}

# json_data = json.dumps(data)  # dict 형식은 dumps로 읽어오기

# print(type(json_data))
# print(json_data)

# json 쓰기
# key, value 추가하고 작성하기
# data["language"] = ["java", "script"]
# with open("data/test1.json", "w") as f:
#     json.dump(data, f, indent=2)  # indent=2 : 들여쓰기

# test1.json 읽어오기
# with open("data/test1.json", "r") as f:
#     json_data = json.load(f)

#     print(json_data)

# users.json 읽어오기 전체적으로 배열로 되어 있음. 한사람의 대한 정보가 {중괄호로 묶여있음}.
with open("data/users.json", "r") as f:
    json_data = json.load(f)

    # print(json_data)
    for person in json_data:
        for k, v in person.items():
            print(k, v)

        print()

print()
