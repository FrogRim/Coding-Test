arr = list(map(int, input().split()))
even_num = 0
odd_num = 0
arr_th = []

for i in range(0,len(arr)):
    if i % 2 != 0:
        even_num += arr[i]
    else:
        odd_num += arr[i]
    
if odd_num > even_num:
    print(odd_num - even_num)
else:
    print(even_num- odd_num)


