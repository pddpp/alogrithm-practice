class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        # Two pointer basic function, implemented with defects.
        if not nums: # need to consider [] case
            return -1
        minLen = sys.maxint
        start = end = 0
        sum = 0
        while end < len(nums):
            sum += nums[end]
            while start <= end and sum >= s: #!!!!!!!! updating a sum variable to keep track of local sum, instead of using build-in function sum(int1, int2)
                minLen = min(minLen, end+1-start) 
                sum -= nums[start] #!!!!!!!!Line 16 and 17: update sum before adding pointer, otherwise is wrong!
                start += 1
            end += 1
        if minLen == sys.maxint: # need to consider no answer case
            return -1
        return minLen
                
