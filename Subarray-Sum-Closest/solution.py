class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    # classic local/global dp problem, challenge is return is the start and end, index, so we need to keep and update that information as well.
    # need to init the variables with A[0] instead of [-1, -1]
    def continuousSubarraySum(self, A):
        # Write your code here
        local_max = A[0] # use local_max and global_max for name, instead of local, global
        global_max = A[0]
        result = [0, 0]
        local_start = 0
        local_end = 0
        for i in xrange(1, len(A)):
            if local_max >= 0:
                local_end = i
                local_max = local_max+A[i]
            else:
                local_start, local_end = i, i
                local_max = A[i]
            if local_max >= global_max:
                result = [local_start, local_end]
                global_max = local_max
            else:
                 global_max = global_max
        return result
