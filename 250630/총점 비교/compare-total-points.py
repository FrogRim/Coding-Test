n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Student:
    def __init__(self,name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []

for i in range(n):
    students.append(Student(name[i],score1[i],score2[i],score3[i]))

# 점수의 총합 기준 오름차순
students.sort(key=lambda x: x.kor + x.eng + x.math) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name, student.kor, student.eng, student.math)

