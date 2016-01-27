class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        # typical two pointer question, implemented with minor defect
        if not heights:
            return 0
        left = 0
        right = len(heights)-1
        result = 0
        while left < right:
            area = (right-left)*min(heights[left], heights[right]) # !!!right-left not heights[right]-heights[left]!!!!!!!!!!
            result = max(result, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
