n = int(input())

prod = 0
temp = n
for i in range(1, n+1):

    temp = temp // i
    prod += 1

    if  temp <= 1:
        print(prod)
        break
    
    