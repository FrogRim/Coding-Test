

inputs = list(map(int, input().split()))
list_ = [(x + 3 if x % 2 == 1 else x // 2) for x in inputs[:inputs.index(0)]]


for i in list_:
    print(i ,end=" ")