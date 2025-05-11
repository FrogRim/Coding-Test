arr = list(map(int, input().split()))

arr_l=[]

for i in arr:
    if i % 3 !=0:
        arr_l.append(i)
    else:
        break

print(arr_l[-1])
