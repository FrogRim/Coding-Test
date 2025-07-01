n = int(input())
sequence = list(map(int, input().split()))

s = set()
# Please write your code here
class element:
    def __init__(self,num,cur):
        self.num = num+1
        self.cur = cur+1

seq_sort = sequence.copy()

seq_sort.sort()

result = []

for i in range(n):

    tmp = seq_sort.index(sequence[i])

    if tmp not in s:
        result.append(element(i,tmp))
        s.add(tmp)
    else:
        for k in range(seq_sort.count(sequence[i])):
            if tmp + k not in s:
                result.append(element(i,tmp+k))
                s.add(tmp + k)
                break
            
    
for t in result:
    print(f"{t.cur}", end=" ")
  