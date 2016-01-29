class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        # implemented myself after getting idea from lecture and familar with two pointer question stereotypes, two defects.
        def isValid(dicS, dicT):
            for char, f in dicT.items(): #dicT.items() not dicT
                if char not in dicS or f > dicS[char]:
                    return False
            return True
        result = ""
        start = end = 0
        dicS = {}
        dicT = {}
        for char in target:
            if char not in dicT:
                dicT[char] = 1
            else:
                dicT[char] += 1
        while end < len(source):
            if source[end] not in dicS: #!!!!!dicS[source[end]] = 1, not dicS[end] = 1
                dicS[source[end]] = 1
            else:
                dicS[source[end]] += 1
            while isValid(dicS, dicT) and start <= end:
                if len(result) == 0 or end-start+1 < len(result):
                    result = source[start:end+1]
                if dicS[source[start]] == 1:
                    del dicS[source[start]]
                else:
                    dicS[source[start]] -= 1
                start += 1
            end += 1
        return result
