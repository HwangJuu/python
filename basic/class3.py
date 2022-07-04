print()
# 클래스 변수 - 반드시 선언 필요, 클래스 이름. 클래스 변수 사용
class UserInfo:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0

    def __init__(self, name, age) -> None:
        # self를 붙이면 객체가 개별로 가지고 있는 멤버 변수
        self.name = name
        self.age = age
        # self.user_cnt += 1
        # 클래스 변수 : class이름을 붙이면 static 과 같은 개념
        UserInfo.user_cnt += 1

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)

    def __del__(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("홍길동", 25)
user2 = UserInfo("성춘향", 26)

print(user1.user_info())
print(user2.user_info())

print("현재 생성된 User {}명".format(UserInfo.user_cnt))
# print()
# 객체 삭제
del user1  # __del__호출됨
print("현재 생성된 User {}명".format(UserInfo.user_cnt))

print()
