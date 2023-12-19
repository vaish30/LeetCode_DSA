class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + solve(i - 1, j - 1)
            else:
                memo[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))
            return memo[(i, j)]
        
        memo = {}
        return solve(len(text1) - 1, len(text2) - 1)