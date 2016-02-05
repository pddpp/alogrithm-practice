class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        # dp[i][j] True if s[i:j+1] is PS
        # Since the O(n) answer is not easy, this O(n^2) solution is acceptable
        # implemented with minor defects myself
        def search(i, j):
            if visited[i][j]:
                return dp[i][j]
            if s[i] == s[j]:
                if i+1 > j-1: #!!!!!!need this
                    return True
                dp[i][j] = search(i+1, j-1)
            else:
                dp[i][j] = False
            visited[i][j] = True 
            return dp[i][j]
        dp = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        visited = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)):
            dp[i][i] = True
            visited[i][i] = True
        result = ""
        for i in xrange(len(s)):
            for j in xrange(len(s)):
                if search(i, j) and j-i+1 > len(result):
                    result = s[i:j+1]
        return result #!!!!!!! be careful whether to return the substring, or max_length or index
