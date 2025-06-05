terms=[]
while True:

    term = input()
    

    if term == '0':
        print(len(terms))
        [print(terms[x]) for x in range(len(terms)) if x % 2 == 0]
        
        break
    
    terms.append(term)

 