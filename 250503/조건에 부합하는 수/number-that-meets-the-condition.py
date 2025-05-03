n = int(input())


for i in range(1, n + 1):
    if ((i % 2 != 0) or (i % 4 == 0)) and ((i // 8) % 2 != 0) and (i % 7 > 3):
        print(i, end=' ')
        
    else:
        continue 
        
   
   


