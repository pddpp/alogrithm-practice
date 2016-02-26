class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # helper function for subsets(self, S) 
        def subsetsHelper(lst=[], pos=0): ###!!! Note local function need to be defined before calling in line19
            result.append(lst[:])
            for i in xrange(pos, len(S)):# Just use S directly even if not a input
                lst.append(S[i])
                subsetsHelper(lst[:], i+1)
                lst.pop()
        # write your code here
        if S is None:
            return None
        S.sort() # to let it pass, need sort
        result = []
        subsetsHelper() #! subsetsHelper() instead of self.subsetsHelper()
        return result
        
