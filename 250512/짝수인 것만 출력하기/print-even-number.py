n = int(input())

list_ = [int(x) for x in input().split() if int(x) % 2 == 0]

for i in list_:
    print(i,end=" ")
