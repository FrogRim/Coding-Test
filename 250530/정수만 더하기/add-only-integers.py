s = input()

result= 0

for k in s:
    if k.isdigit() == True:
        result += int(k)

print(result)