s,q = input().split(" ")
arr = list(s)


for i in range(int(q)):
    order,first,second = input().split(" ")
    

    if int(order) == 1:
        temp = arr[int(first)-1]
        arr[int(first)-1] = arr[int(second)-1]
        arr[int(second)-1] = temp
        for i in arr:
            print(i, end="")
        
    else:
       
        for i in range(len(s)):
            if arr[i] == first:
                arr[i] = second
      
        for i in arr:
            print(i, end="")    
    print()    
    

