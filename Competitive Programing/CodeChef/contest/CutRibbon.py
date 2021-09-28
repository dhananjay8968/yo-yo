def solve(n, k, mod, dp):
     
    # Base case if no-solution exist
    if (n < 0):
        return 0
 
    # Condition if a solution exist
    if (n == 0):
        return 1
 
    # Check if already calculated
    if (dp[n] != -1):
        return dp[n]
 
    # Initialize counter
    cnt = 0
    for i in range(2, k + 1, 2):
         
        # Recursive call
        cnt = ((cnt % mod +
                solve(n - i, k, mod, dp) %
                                    mod) % mod)
                                    
    # Store the answer
    dp[n] = cnt
 
    # Return the answer
    return int(cnt)

t = int(input())

for i in range(t) :
    n,k = list(map(int, input().split()))
    mod = (10**9) + 7
    dp = [-1]*(n+1)
    print(solve(n,k,mod,dp))