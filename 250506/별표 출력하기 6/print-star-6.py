n = int(input())
for i in range((2*n-1)//2+1): 
    for j in range(i):
        print(" ", end=" ")
    for j in range((2*n-1)-2*i):
        print("*", end=" ")
    print()

for i in range((2*n-1)// 2): 
    for j in range((2*n//2)-(i+2)):
        print(" ", end=" ")
    for j in range(2*i+3):
        print("*", end=" ")
    print()
