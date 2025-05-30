a= input()
b= input()

a1=""
a2=""
for i in a:
    if i.isdigit() == False:
        continue
        
    else:
        a1 += "".join(i)
        

for i in b:
    if i.isdigit() == False:
        continue
    else:
        a2 += "".join(i)

print(int(a1)+ int(a2))

