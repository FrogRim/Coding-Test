s = input()
start = 0

if len(s) % 2 == 0:
    print(s[-1:-len(s)-1:-2])
else:
    print(s[-2:-len(s)-1:-2])

