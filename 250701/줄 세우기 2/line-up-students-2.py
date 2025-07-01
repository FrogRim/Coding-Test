n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
# n = int(input())
# students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
students.sort(key=lambda x: (x[0],-x[1],x[2])) 

for i in students:
    print(f"{i[0]} {i[1]} {i[2]}")


# 정렬 이후 등수별 학생 번호 출력
# for (height,weight,number) in enumerate(students, start=1):
#     print(f"{student.height} {student.weight} {student.number}")

