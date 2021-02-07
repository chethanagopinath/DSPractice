class Solution:
    def climb_stairs(self, n):
        # Climbing stairs where the child can hop 1, 2, or 3 steps at a time. Number of ways to reach nth step?

        # https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_08/p01_triple_step.py

        # Let's do the bottom-up approach first - DP
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp)
        return dp[n]

        # Top-down approach - Sometimes called Memoisation
        # memo = {}

        # self.climb_stairs_top_down(n, memo)
        # print(memo)
        # return memo[n]

    def climb_stairs_top_down(self, n, memo):
        # base case -> if n is 0, return 1
        if n < 0:
            return 0
        # From 0, there is only one way to climb
        if n == 0:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.climb_stairs_top_down(n - 1, memo) + self.climb_stairs_top_down(
            n - 2, memo) + self.climb_stairs_top_down(n - 3, memo)
        return memo[n]


sol = Solution()
print(sol.climb_stairs(6))
