class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        def subsetsHelper(lst=[], pos=0):
            result.append(lst[:])
            for i in xrange(pos, len(S)):
                if i != pos and S[i] == S[i-1]: #!!! i != pos, otherwise [1,1] will only out put [[], [1]] instead of [[], [1], [1,1]]
                    continue
                lst.append(S[i])
                subsetsHelper(lst[:], i+1)
                lst.pop()
        # write your code here
        if S is None:
            return []
        S.sort()
        result = []
        subsetsHelper()
        return result

    # helper function for subsetsWithDup(S)
    '''def subsetsHelper(self, S, result, lst=[], pos=0):
        result.append(lst[:])###!!!!!!!!!!!!!!!!!!!!!!!!! append list by value not reference!!!!!!!!!!!!
        tmp = None
        for i in xrange(pos, len(S)):
            if tmp == S[i]:
                continue
            lst.append(S[i])
            self.subsetsHelper(S, result, lst, i+1)##### "i+1" not pos+1
            tmp = lst.pop()
    '''
