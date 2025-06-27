
MAX_N = 5

class Agent:
    def __init__(self, codename, score=0):
        self.codename = codename
        self.score = score

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

agents = []
for i in range(5):
    tmp_name = codenames[i]
    tmp_score = scores[i]
    agents.append(Agent(tmp_name,tmp_score))


agents.sort(key= lambda x: x.codename)

i = agents[0]
print(f"{i.codename} {i.score}")



