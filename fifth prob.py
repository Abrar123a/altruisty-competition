n=int(input())
arr=list(map(int,input().split()))
price=int(input())
maxi=0
l=0
r=0
while r<n:
    if sum(arr[l:r+1])>price:
        l+=1
    else:
        r+=1
    maxi=max(maxi,r-l)
print(maxi)
