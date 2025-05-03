a = int(input())
prod = 1
for i in range(1, 10):

    prod *= i
    
    if  prod >= a:
        print(i)
        break
    
    