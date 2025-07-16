N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code he
flag = [i > 0 for i in arr]

cnt = 0
tmp = 0
    
for i in range(N):
    if  i == 0 or flag[i] != flag[i - 1] :
        cnt = 1        
    else:
        cnt += 1
    
    if cnt > tmp:
        tmp = cnt
        
        

print(tmp)