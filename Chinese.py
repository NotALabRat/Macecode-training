n=int(input())
day=list(map(int, input().split()))
night=list(map(int, input().split()))
hour=int(input())

day.sort()
night.sort(reverse=True)

extra=0
for i in range(n):
    if day[i]+night[i]>hour:
        
        extra=extra+abs(hour-(day[i]+night[i]))
        
print(extra*100)

        
        
        
                
                
            
