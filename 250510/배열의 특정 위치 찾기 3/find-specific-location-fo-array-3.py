arr = list(map(int, input().split()))

arr_l=[]

for i in arr:
    if i !=0:
        arr_l.append(i)
    else:
        break

print(arr_l[-1] + arr_l[-2]+ arr_l[-3])
