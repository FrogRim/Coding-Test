s = input()

for x in s:
    if 'A' <= x and x <= 'Z':
        print(x.lower(),end="")
    else:
        print(x.upper(),end="")
        