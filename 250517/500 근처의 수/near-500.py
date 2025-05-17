a = [int(x) for x in input().split()]

over = []
under = []

for i in a:
    if i < 500:
        under.append(i)
    elif i > 500:
        over.append(i)


print(f"{max(under)} {min(over)}")