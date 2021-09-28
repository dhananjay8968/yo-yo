import math
import bisect


def SieveOfEratosthenes(n):
    n = int(math.sqrt(n))
    prime_numbers = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
       
        if (prime[p] == True):
             
            
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
  
    for p in range(n + 1):
        if prime[p]:
            prime_numbers.append(p)

    return prime_numbers

t = int(input())

for i in range(t) :
    n = int(input())
    ans = 0

    if n == 1 :
        print(0)
        continue


    A = SieveOfEratosthenes(n)
    A.pop(0)

    x = int(math.log(n,2))
    x += 1
    ans += bisect.bisect(A,x)
    print(ans)
   
    

    for i in A :
        x = int(math.log(n,i))
        x += 1


        a = bisect.bisect(A, x)
        ans += a 

    print(ans)
