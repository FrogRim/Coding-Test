s = input()
arr = list(s)

for k in range(len(s)):
    if s[k] == s[1]:
        arr[k] = s[0]

s = ''.join(arr)
print(s)
