A,B = map(int,input().split())
n = A//B
n_f = A%B

print(n, end="")
print(".", end="")

for _ in range(20):
    n_f *=10
    x  = n_f//B
    print(x,end="")
    n_f = n_f%B

