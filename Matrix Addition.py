n=input().split()

m1=[]
m2=[]


for i in range(int(n[0])):
    a=input().split()
    m1.append(a)
        
for i in range(int(n[0])):
    a=input().split()
    m2.append(a)
    
print("First Matrix:")
for i in range(int(n[0])):
    for j in range(int(n[1])):
        print(m1[i][j],end=" ")
    print("")
    
print("Second Matrix:")
for i in range(int(n[0])):
    for j in range(int(n[1])):
        print(m2[i][j],end=" ")
    print("")
    
    

        
res=[]
        
for i in range(int(n[0])):
    for j in range(int(n[1])):
        res.append(int(m1[i][j])+int(m2[i][j]))

ind=0
print("Sum of the two matrices is:")

for i in range(int(n[0])):
    for j in range(int(n[1])):       
        print(res[ind],end=" ")
        ind=ind+1
    print("")
