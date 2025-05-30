s = input()

result=[]

for k in s:
    if k.isalpha() == True or k.isdigit() == True:
        result.append(k)

for i in result:
    if k.isalpha() == True:
        print(i.lower(),end="")
    else:
        print(i,end="")