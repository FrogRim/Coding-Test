a,b = map(int,input().split())

elem = [int(i) for i in input().split()]

idx = -1

for _ in range(b):
    query = [int(i) for i in input().split()]
    
    if query[0] == 1:
        print(elem[query[1]-1])

    
    elif query[0] == 2:
        for i, char in enumerate(elem):
            if char == query[1]:
                idx = i
                break

        if idx == -1:
            print("0")
        else:
            print(idx+1)
    
    elif query[0] == 3:
        result = elem[(query[1]-1):(query[2])]

        for k in result:
            print(k,end=" ")
        print()

    



