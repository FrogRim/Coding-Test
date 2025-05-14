a,b = map(int,input().split())

elem1 = [int(i) for i in input().split()]

elem2 = [int(i) for i in input().split()]

cnt = 0
arrs = []

while cnt < a:
    arrs.append(elem1[cnt:(cnt+(b))])
    #print(elem1[cnt:(cnt+(b-1))])
    cnt += 1
   

if elem2 in arrs:
    print('Yes')
else:
    print("No")



