class Solution:
    def strStr(self, source, target):
        # helper function for strStr
        def strStrHelper(i, j):
            if j == len(target):
                return True
            if source[i] != target[j]:
                return False
            else:
                return strStrHelper(i+1, j+1)
        # write your code here
        #if source is None or target is None:
        #    return -1
        #if len(source) == 0 and len(target) == 0:
        #    return 0
        if not source or not target or len(source) < len(target):
            if target == "": # remember to consider this situation
                return 0
            return -1
        for i in xrange(len(source)-len(target)+1):
            if strStrHelper(i, 0):
                return i
        return -1
