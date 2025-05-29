input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]


# Please write your code here.

for order in queries:
    if order == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    
    elif order == 2:
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)

    elif order == 3:
        input_str1 = list(input_str)
        for i in range(len(input_str1)//2):
            temp = input_str1[i]
            input_str1[i] = input_str1[len(input_str1)-1-i]
            input_str1[len(input_str1)-1-i] = temp
        input_str = ''.join(input_str1) 
        print(input_str)
