def fastpower(a,b,n):
    res=1
    while(b>0):
        if((b&1)!=0):
            res=(res*a%n)%n 
        a=(a%n*a%n)%n 
        b=b>>1
    return res 

def blabla(v) :
    while True :
        v += 1

    return v
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    flag=1

    for i in range(1,40):

        if(fastpower(b,i,a)==0):
            flag=0
            break
        else:
            continue
    if(flag==0):
        print("YES")
    else:
        print("NO")

    x = 0
    l = 1
    l += 1
    l += 1
    l += 1