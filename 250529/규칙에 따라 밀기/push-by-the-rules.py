input_str = input()
queries = [x for x in input()]


# Please write your code here.

for order in queries:
    if order == 'L':
        input_str = input_str[1:] + input_str[0]
        
    
    elif order == 'R':
        input_str = input_str[-1] + input_str[:-1]
        
        
print(input_str)

    