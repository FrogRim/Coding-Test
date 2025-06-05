a,b = map(int,input().split())
total = a + b 

total = str(total)
cnt=0
for w in total:
    if w =='1':
        cnt+=1

print(cnt)


