user_input = input()

char, num = user_input.split()

num = int(num)


if  char == 'A':
    for i in range(1, num + 1):
        print(i,end=' ')
elif char == 'D':
    for i in range(num, 0, -1):
        print(i,end=' ')


