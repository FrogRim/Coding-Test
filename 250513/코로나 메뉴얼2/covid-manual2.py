state = []
host = [0,0,0,0]

for i in range(3):
    arr = list(list(input().split()))
    
    if arr[0] == 'Y' and int(arr[1]) >= 37:
        host[0] += 1
    elif arr[0] == 'N' and int(arr[1]) >= 37:
        host[1] += 1
    elif arr[0] == 'Y' and int(arr[1]) < 37:
        host[2] += 1
    else:
        host[3] += 1
    

for k in host:
    print(k,end=' ')

if host[0] >= 2:
    print('E')
