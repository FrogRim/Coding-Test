n = int(input())

list_ = [x for x in input().split() if x % 2 == 0]

for i in range(n):
    print(list_[i] ,end=" ")