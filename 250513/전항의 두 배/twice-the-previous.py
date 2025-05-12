a,b = map(int,input().split())

arr = []
arr.append(a)
arr.append(b)
for i in range(2,10):
    c = 2*arr[i-2]+arr[i-1]
    arr.append(c)
    

for i in arr:
    print(i,end=" ")