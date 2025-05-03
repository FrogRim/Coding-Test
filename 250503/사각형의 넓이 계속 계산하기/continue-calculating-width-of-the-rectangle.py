cnt = []

while True:
   
    a_str, b_str, flag = input().split()

    
    a = int(a_str)
    b = int(b_str)

    
    cnt.append(a * b)

    
    if flag == 'C':
        break

for v in cnt:
    print(v)
