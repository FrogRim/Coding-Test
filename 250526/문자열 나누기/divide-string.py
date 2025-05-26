n = int(input())
arr = []

text = input().split()

tot_str = "".join([x for x in text])

x = 0
while x < len(tot_str):
    print(tot_str[x:x+5])
    x += 5



