class GoUpstairs:
    defcountWays(self, n):
        dp=[0,1,2]
        if(n>2):
            for x in range(3,n):
                dp.append((dp[x-1]+dp[x-2])%1000000007)
        return dp[n-1]
