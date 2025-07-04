N = input()

# Please write your code here.


def convert_2by10(binary):

    binarys = []

    for b in binary:
        binarys.append(int(b))

    num = 0

    for i in range(len(binarys)):
        num = num * 2 + binarys[i]

    return num

def convert_10by2(n):
    digits = []

    while True:
        if n < 2:
            digits.append(n)
            break

        digits.append(n % 2)
        n //= 2

        # print binary number
        

    return digits        


first = convert_2by10(N)

first = first * 17

second = convert_10by2(first)

for s in second[::-1]:
        print(s, end="")