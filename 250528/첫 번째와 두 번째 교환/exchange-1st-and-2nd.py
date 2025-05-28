s = input()
arr = list(s)

zero = s[0]
one = s[1]
for i in range(len(s)):
    if s[i] == zero:
        arr[i] = one
    if s[i] == one:
        arr[i] = zero
     
      
s = ''.join(arr)
print(s)
