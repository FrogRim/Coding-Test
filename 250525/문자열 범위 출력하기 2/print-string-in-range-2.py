given_str = input()
n = int(input())


for i in given_str[len(given_str)-1:len(given_str)-1-n:-1]:
    print(i,end="")
