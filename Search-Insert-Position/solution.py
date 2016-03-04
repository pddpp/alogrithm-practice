class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    # this problem equals to find first position where A[i] >= target
    def searchInsert(self, A, target):
        # write your code here
        if A is None:
            return -1
        if A == []:
            return 0
        start = 0
        end = len(A)-1
        while (start+1 < end):
            mid = (start+end)/2
            if A[mid] < target:
                start = mid
            elif A[mid] == target:
                return mid
            else:
                end = mid
        if A[start] >= target: # be careful here!!!!!!!!!
            return start
        elif A[end] >= target: # here!!!!!!!!!!!
            return end
        else:
            return end+1  # and here !!!!!!!!
        
