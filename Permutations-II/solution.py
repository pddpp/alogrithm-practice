class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # helper function for this unique permutation
        def permuteHelper(lst=[], rmn=nums):
            #rmn_length = len(rmn)
            if not rmn:
                result.append(lst[:])
                return #!!!!!!!!!!!!!!!!!!no return no good!!!!!!!!!
            tmp = None
            for i in xrange(len(rmn)):
                if tmp != rmn[i]:
                    #lst.append(rmn[i])
                    #del rmn[i]
                    lst.append(rmn.pop(i))
                    permuteHelper(lst[:], rmn[:])#!!!!!!!!!!!!!!!need to bring in value not reference for the recursion
                    tmp = lst.pop()
                    rmn.insert(i, tmp)
        # write your code here
        if nums is None:
            return None
        nums.sort()
        result = []
        permuteHelper()
        return result
