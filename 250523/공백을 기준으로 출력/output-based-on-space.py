given_input = input()
given_input1 = input()

texts = []

texts.append(given_input)
texts.append(given_input1)


cnt = 0
for i in texts:
    for j in i:
        if j != " ":
            print(j,end="")


