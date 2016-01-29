class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        # One time pass, with practice of two pointer question before.
        result = 0
        start = end = 0
        dic = {} #store character: frequency pairs
        while end < len(s):
            if s[end] in dic: # step: process end
                dic[s[end]] += 1
            else:
                dic[s[end]] = 1
            while len(dic) > k: # step: while xxx: process start
                if dic[s[start]] != 1 :
                    dic[s[start]] -= 1
                else:
                    del dic[s[start]]
                start += 1 # step: start += 1
            result = max(result, end+1-start) # step: refresh answer 
            end += 1 # step: end += 1
        return result
