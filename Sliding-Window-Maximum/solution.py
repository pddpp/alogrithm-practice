class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        # deque, decreasing queue, coding and debugged myself with many troubles
        result = []
        deque = []
        if not nums:
            return result
        for i in xrange(len(nums)):
            for num in deque: # Delete the element which is too old
                if num[1] < i-k+1:
                    deque.pop(0)
                else:
                    break
            if not deque or nums[i] <= deque[0][0]: # note deque empty case; compare with deque[0][0]
                while deque and deque[-1][0] <= nums[i]: # note deque empty case; to maintain deque's decrease, remove all element smaller than the adding one from deque
                    deque.pop()
            else:
                deque = []
            deque.append([nums[i], i]) # add it to deque anyways
            result.append(deque[0][0])
        return result[k-1:]
