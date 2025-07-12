r=int(input())
c=int(input())
mat=[]
ct=0
for i in range(r):
    row=list(map(int, input().split()))
    mat.append(row)
    
for i in range(r):
    for j in range(c):
        if mat[i][j]<0:
            ct=ct+1
            
print(ct)




    
