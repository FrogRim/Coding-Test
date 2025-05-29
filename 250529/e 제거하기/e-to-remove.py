s = input()
arr = list(s)
arr.pop(s.find('e'))
s = ''.join(arr)
print(s)

