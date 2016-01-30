class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        # use global and local to save time, 
        if not nums: 
            return None
        local_max = [nums[0], 0] #!!!!!!!!initial value is nums[0], not zero and not -sys.maxint
        global_max = [nums[0], 0]
        for i in xrange(1, len(nums)):
            local_max[i%2] = max(nums[i], local_max[(i-1)%2]+nums[i])
            global_max[i%2] = max(local_max[i%2], global_max[(i-1)%2])
        return global_max[(len(nums)-1)%2]
    def maxSubArray2(self, nums):
        # write your code here
        if not nums: # must remeber this question!!
            return None
        maxSub = -sys.maxint
        sumTot = 0 
        minSum = 0
        for val in nums:
            sumTot += val
            maxSub = max(maxSub, sumTot-minSum)
            minSum = min(minSum, sumTot)
        return maxSub
