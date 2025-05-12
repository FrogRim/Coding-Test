n = int(input())

list_ = [int(x) ** 2 for x in input().split()]

for i in range(n):
    print(list_[i] ,end=" ")