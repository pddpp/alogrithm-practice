class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        # Two pointer, many tricky points, need to rewrite again!
        result = 0
        dic = {}
        start = end = 0
        while start <= end and end < len(s):
            while end < len(s) and s[end] not in dic:
                result = max(result, end+1-start)
                dic[s[end]] = end
                end += 1
            if end < len(s):
                tmp = dic[s[end]]+1
                for i in xrange(start, dic[s[end]]+1): #!!+1
                    del dic[s[i]]
                start = tmp # update start basing on original dic[s[end]]
        return result
            
