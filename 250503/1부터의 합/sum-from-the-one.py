a = int(input())
prod = 0
for i in range(1, 101):

    prod += i
    
    if  prod >= a:
        print(i)
        break
    
    