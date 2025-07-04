N, B = map(int, input().split())

# Please write your code here.
binarys = []

def from_binary(n,b):
    
    if n < b:
        binarys.append(n)
        return binarys

    binarys.append(n % b)
    

    return from_binary(n//b,b)   

result = from_binary(N,B)
num = 0

for i in range(len(result)):
    num += (10 ** i) * result[i]

print(num)








