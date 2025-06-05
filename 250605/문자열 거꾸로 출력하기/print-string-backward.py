
while True:

    term = input()
    term1 = list(term)
    if term == 'END':
        break

    else:
        for i in range(len(term1)):
            term1[i] = term[len(term)-i-1]
        
        term="".join(term1)

        print(term)

