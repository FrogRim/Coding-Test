s = input()
arr = list(s)

while len(arr) > 1:
    q = int(input())
    if q > len(arr):
        arr.pop(-1)
    else:
        arr.pop(q)
    s = "".join(arr)
    print(s)

