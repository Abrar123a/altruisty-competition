n=int(input())
arr=list(map(int,input().split()))
nmap={}
for i in arr:
    if i in nmap:
        nmap[i]+=1
    else:
        nmap[i]=1

for i in nmap.keys():
    if nmap[i]==1:
        print(i,end=' ')
