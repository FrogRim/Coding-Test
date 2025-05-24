arr = [ "apple", "banana", "grape", "blueberry","orange"]
n = input()
cnt = 0
for term in arr:

    if term[2] == n or term[3] == n:
        print(term)
        cnt += 1

print(cnt)
