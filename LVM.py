n=int(input())

instructions=[]
for i in range(n):
    instructions.append(input().split())

stack=[]
register = 0
i = 0

while i<len(instructions):
    instr =instructions[i]

    if instr[0]=='PUSH':
        stack.insert(0,int(instr[1]))  
        i+= 1

    elif instr[0]=='STORE':
        register=stack.pop(0)  
        i+= 1

    elif instr[0]=='LOAD':
        stack.insert(0,register)  
        i+= 1

    elif instr[0]=='PLUS':
        a=stack.pop(0)
        b=stack.pop(0)
        stack.insert(0,a+b)
        i+= 1

    elif instr[0]=='TIMES':
        a=stack.pop(0)
        b=stack.pop(0)
        stack.insert(0,a*b)
        i+= 1

    elif instr[0]=='IFZERO':
        value=stack.pop(0)
        if value==0:
            i=int(instr[1])
        else:
            i+= 1

    elif instr[0]=='DONE':
        print(stack[0])  
        break
