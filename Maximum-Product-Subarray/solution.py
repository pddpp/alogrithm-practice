class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        # get the state function before writing the code, and it will be fast and bug free
        if not nums:
            return None
        local_min = [nums[0], 0]
        local_max = [nums[0], 0]
        global_max = [nums[0], 0]
        for i in xrange(1, len(nums)):
            local_max[i%2] = max(local_max[(i-1)%2]*nums[i], nums[i], local_min[(i-1)%2]*nums[i])
            local_min[i%2] = min(local_min[(i-1)%2]*nums[i], nums[i], local_max[(i-1)%2]*nums[i]) #!!! typo, the second variable is local_max[(i-1)%2] not local_min[(i-1)%2
            global_max[i%2] = max(global_max[(i-1)%2], local_max[i%2])
        return global_max[(len(nums)-1)%2]
