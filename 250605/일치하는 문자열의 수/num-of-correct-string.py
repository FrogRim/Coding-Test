n,A = input().split()

n = int(n)

cnt=0

for _ in range(n):
    term = input()
    if term == A:
        cnt+=1
        
print(cnt)