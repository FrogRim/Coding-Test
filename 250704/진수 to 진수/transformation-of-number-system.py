a, b = map(int, input().split())
n = input()

# Please write your code here.
def convert_a_to_10(n,k):

    binarys = []

    for b in n:
        binarys.append(int(b))

    num = 0

    for i in range(len(binarys)):
        num = num * k + binarys[i]

    return num

def convert_b_to_a(n,k):
    digits = []

    while True:
        if n < 2:
            digits.append(n)
            break

        digits.append(n % k)
        n //= k

        

    return digits        


first = convert_a_to_10(n,a)

second = convert_b_to_a(first,b)

for s in second[::-1]:
        print(s, end="")