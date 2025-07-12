n,d=list(map(int,input().split()))
weights=list(map(int,input().split()))
weights.sort(reverse=True)
jam=0
for i in range(d):
    jam=sum(weights[:d])
print(jam)
