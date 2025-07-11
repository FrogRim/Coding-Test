n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []


for i in range(n):
    students.append(Student(name[i],korean[i],english[i],math[i]))
    

students.sort(key=lambda x: (-x.kor,-x.eng,-x.math)) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name,student.kor, student.eng, student.math)

