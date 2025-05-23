text=[]
maxlen = 0
minlen = 21

for _ in range(3):
    n = input()
    if len(n) > maxlen:
        maxlen = len(n)
    if len(n) < minlen:
        minlen = len(n)

print(maxlen - minlen)