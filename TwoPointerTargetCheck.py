n=int(input())
l=input().split()
sum=int(input())

flag=0
for i in range(n):
    if str(sum-int(l[i])) in l[0:i]+l[i+1:]:
        flag=1
        break
if flag==0:
    print("No")
else:
    print("Yes")
