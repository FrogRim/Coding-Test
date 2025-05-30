s = input()

result=[]

for k in s:
    if k.isalpha() == True:
        result.append(k)

for i in result:
    print(i.upper(),end="")