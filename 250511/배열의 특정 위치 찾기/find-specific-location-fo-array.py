arr = list(map(int, input().split()))
even_num = 0
arr_th = []

for i in range(0,len(arr)):
    if i % 2 != 0:
        even_num += arr[i]
    
    if (i+1) % 3 == 0:
        arr_th.append(arr[i])
    
print(even_num,end=" ")
print(f"{sum(arr_th)/len(arr_th):.1f}")


