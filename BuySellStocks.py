n=int(input())
stock= list(map(int, input().split()))

max_profit=float('-inf')
buy=0
sell=1

while sell< n :
    if stock[buy]<stock[sell]:
        max_profit=max(max_profit,(stock[sell]-stock[buy]))   
    else:
        buy=sell
        
    sell=sell+1
    
print(max_profit)
        
        
        
        
    



        
    
        
    

