n = int(input())
for i in range(n):         
    for j in range(1 + i): 
        print("*", end="")
    print("\n")
for i in range(n):         
    for j in range((n-1) - i): 
        print("*", end="")
    print("\n")
    
