cnt = 0
total = 0
avg = 0
while True:
    n = int(input())
    if(n <= 29 and n >= 20):
        total += n
        cnt += 1
    else:
        avg = total/cnt
        break
    






print(f"{avg:.2f}")