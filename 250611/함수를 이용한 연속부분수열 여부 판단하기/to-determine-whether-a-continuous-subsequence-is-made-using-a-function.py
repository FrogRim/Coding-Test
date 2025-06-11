n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def check(a,b):
    max_lst = a 
    min_lst = b 

    for i in range(len(max_lst)):
        temp = max_lst[i:i+len(min_lst)]
        
        if temp == min_lst:
            return True
    
    return False

print("Yes" if check(a,b) == True else "No")