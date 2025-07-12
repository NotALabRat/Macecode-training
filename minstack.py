n=int(input())
stack=[]
for i in range(n):
    q=list(map(int, input().split()))
    if q[0]==0:
        stack.append(q[1])
    elif q[0]==1:
        stack.pop(len(stack)-1)
    
    elif q[0]==2:
        ele=stack[len(stack)-1]
        print(ele)
    elif q[0]==3:
        print(min(stack))
        
    
    
