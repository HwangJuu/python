print()
# 학생 3명의 정보 입력, 출력하고 싶음.
# 클래스를 사용해도되고, 안해도 됨.
# 안해도 될 땐 변수 선언 이용

# 변수
# 학생 1
student_name1 = "Kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [{"gender": "male"}, {"score1": 97}, {"score2": 88}]

# 학생 2
student_name2 = "Park"
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [{"gender": "female"}, {"score1": 87}, {"score2": 96}]

# 학생 3
student_name3 = "Choi"
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [{"gender": "male"}, {"score1": 66}, {"score2": 78}]

# 변수 사용은 효율성이 떨어짐
# print(
#     "이름: %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name1, student_number_1, student_grade_1, student_detail_1)
# )
# print(
#     "이름: %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name2, student_number_2, student_grade_2, student_detail_2)
# )
# print(
#     "이름: %s, 학번 : %d, 학년 : %d, 학생정보 : %s"
#     % (student_name3, student_number_3, student_grade_3, student_detail_3)
# )


# list : 모아서 처리하는 형태인지, 다양한 자료구조, 서로 다른 내용도 한번에 담아서 처리 가능

# student_name_list = ["Kim", "Park", "Choi"]
# student_numbers_list = [1, 2, 3]
# student_grade_list = [1, 2, 3]
# student_details_list = [
#     {"gender": "male", "score1": 97, "score2": 88},
#     {"gender": "female", "score1": 87, "score2": 96},
#     {"gender": "male", "score1": 66, "score2": 78},
# ]
# # # 삭제
# del student_name_list[1]
# del student_numbers_list[1]
# del student_grade_list[1]
# del student_details_list[1]

# # # 전체 출력
# print(student_name_list)
# print(student_numbers_list)
# print(student_grade_list)
# print(student_details_list)
# print()

# # # 특정 학생만 출력
# print(student_name_list[0])
# print(student_numbers_list[0])
# print(student_grade_list[0])
# print(student_details_list[0])


# 클래스
class Student:  # 괄호는 필수 아님
    #  __init__: 자바의 생성자와 같은 개념, self : this와 같은 개념
    def __init__(self, name, number, grade, details):
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    # toString()개념
    def __str__(self):
        return "name : {}, number : {}, grade : {}, details : {}".format(
            self.name, self.number, self.grade, self.details
        )


# 객체 생성
student1 = Student("Kim", 1, 1, {"gender": "male", "score1": 97, "score2": 88})
student2 = Student("Park", 2, 2, {"gender": "female", "score1": 87, "score2": 96})
student3 = Student("Choi", 3, 3, {"gender": "male", "score1": 66, "score2": 78})

# <__main__.Student object at 0x0000022D16EAFD30> 해당 객체에 포함된 16진수 값 출력. 주소값 출력
print(student1)
print(student2)
print(student3)


print()
