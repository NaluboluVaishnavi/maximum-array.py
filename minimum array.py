a = list(map(int,input().split()))
mx = -999
mx2 = -999

#max1
for i in a:
    if i>mx:
        mx = i
#max2
for i in a:
    if i>mx2 and i!=mx:
        mx2 = 1

avg = (mx + mx2)/2
ans = 0
for i in a:
    if i>avg:
        ans += i
print(ans)            
