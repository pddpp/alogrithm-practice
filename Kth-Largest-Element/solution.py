class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        # Bubble sort is time consuming, use two pointer and quick sort
        # This question needs review, it is a two pointer question and use the module of quick sort from "partition array"
        def kthLargestHelper(start, end): 
            pos = quicksort(start, end) # put A[start] to correct position and return the position
            if pos == len(A)-k: # kth integer is A[k-1]
                return A[pos]
            elif pos < len(A)-k:
                return kthLargestHelper(pos+1, end) #!!!!!!!!!!!!!!!!!!don't forget return!!!!!!!!!!!!!
            else:
                return kthLargestHelper(start, pos-1) #!!!!!!!!!!!!don't forget return!!!!!!!!!!!!!!

        def quicksort(left, right):
            start = left+1 #!!!!!!start from left+1
            end = right
            target = A[left]
            while start <= end:
                while start <= end and A[start] <= target: #<=
                    start += 1
                while start <= end and A[end] >= target: #<=
                    end -= 1
                if start <= end:
                    tmp = A[start]
                    A[start] = A[end]
                    A[end] = tmp
            temp = A[left] #!!!!!!!!!! without this swap, the target element won't be in the correct position, even if the return index 'end' is correct
            A[left] = A[end]
            A[end] = temp
            return end

        if not A or len(A) < k:
            return None
        result = kthLargestHelper(0, len(A)-1)
        return result
            
