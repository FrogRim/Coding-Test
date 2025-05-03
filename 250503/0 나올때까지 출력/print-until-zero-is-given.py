sum_val = []
while True:
    n = int(input())
    if(n != 0):
        sum_val.append(n)
    else:
        for i in sum_val:
            print(i)
        break
    
