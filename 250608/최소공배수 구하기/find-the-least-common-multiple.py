n, m = map(int, input().split())

# Please write your code here.
def print_rect(n,m):
    result1 = []
    result2 = []
    for i in range(1,m):
        result1.append(n*i)
            
    for i in range(1,n):
        result2.append(m*i)
          
    
    total = [x for x in result1 if x in result1 and x in result2] 
    print(min(total))



print_rect(n,m)
