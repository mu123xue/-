
def abaaba(n,m):
    if  m==1 or n==m:
        return 1
    else:
        return abaaba(n-1,m-1)+m*abaaba(n-1,m)
n=int(input("qing"))
result=0
for m in range(1,n+1,1):
  result=result+abaaba(n,m)
print(result)