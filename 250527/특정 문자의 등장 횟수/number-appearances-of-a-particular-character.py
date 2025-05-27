s = input()
length = len(s)

cnt1 = 0
cnt2 = 0

for i in range(length - 1):
    if s[i:i + 2] == 'ee':
        cnt1 += 1
    if s[i:i + 2] == 'eb':
        cnt2 += 1

print(f"{cnt1} {cnt2}")        
