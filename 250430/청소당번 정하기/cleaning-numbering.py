cnt1 = 0
cnt2 = 0
cnt3 = 0

n = int(input())
for i in range(1,n+1):
    clear = False

    if i % 12 == 0 and clear == False :
        cnt3 += 1
        clear = True

    if i % 3 == 0 and clear == False:
        cnt2 += 1
        clear = True
    
    if i % 2 == 0 and clear == False:
        cnt1 += 1
        clear = True
    
print(f"{cnt1} {cnt2} {cnt3}")
