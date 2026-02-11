t,x=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i>x:
        c+=1
print(t+c)
