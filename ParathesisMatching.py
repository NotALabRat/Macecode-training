s=input()
stack=[]

for i in s:
    if i=='}':
        if '{' in stack:
            stack.remove('{')
        else:
            stack.append('}')

            
    else:
        stack.append('{')
        
    
        
if len(stack)>0:
    print("Not Matching")
else:
    print("Matching")
            
