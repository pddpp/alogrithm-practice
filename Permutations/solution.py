class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    #Not one time pass, but must master this question together with subset I II and permutation II
    def permute(self, nums):
        # write your code here
        def permute_helper(lst, rmn):
            if not rmn:
                result.append(lst[:])
                return
            for i in xrange(len(rmn)): #!!!!!!!!!!!!!!!!!!!!!!!!!len of rmn not len of lst!!!!!!!!!!!!!!!!
                #tmp = rmn[i]
                #del rmn[i]
                tmp = rmn.pop(i)
                lst.append(tmp)
                permute_helper(lst[:], rmn[:]) # need to deep copy!!!!!!!!!!!!!
                rmn.insert(i, tmp)
                lst.pop()
        result = []
        if not nums:
            return []
        permute_helper([], nums)
        return result
