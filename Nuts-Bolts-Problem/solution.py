# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    # idea come from lecture and implement myself basing on quick sort with only one defect. See if can get code more concise next time.
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        def sortHelper(start, end, botNut):
            if start == end:
                return
            pos = partition(start, end, botNut)
            if start != pos:
                sortHelper(start, pos-1, botNut)
            if pos != end:
                sortHelper(pos+1, end, botNut)
        def partition(start, end, botNut):
            if botNut:
                target = bolts[start]
                target_nut = None
                left = start+1
                right = end
                # find the match nuts for target bolt
                for nut in nuts:
                    if compare.cmp(nut, target) == 0:
                        target_nut = nut
                        break
                while left <= right:
                    while left <= right and compare.cmp(target_nut, bolts[left]) != -1:
                        left += 1
                    while left <= right and compare.cmp(target_nut, bolts[right]) != 1:
                        right -= 1
                    if left <= right:
                        tmp = bolts[left]
                        bolts[left] = bolts[right]
                        bolts[right] = tmp
                tmp = bolts[start]
                bolts[start] = bolts[right]
                bolts[right] = tmp
                return right
            else:
                target = nuts[start]
                target_bolt = None
                left = start+1
                right = end
                # find the match nuts for target bolt
                for bolt in bolts:
                    if compare.cmp(target, bolt) == 0:
                        target_bolt = bolt
                        break
                while left <= right:
                    while left <= right and compare.cmp(nuts[left], target_bolt) != 1:
                        left += 1
                    while left <= right and compare.cmp(nuts[right], target_bolt) != -1:
                        right -= 1
                    if left <= right:
                        tmp = nuts[left]
                        nuts[left] = nuts[right]
                        nuts[right] = tmp
                tmp = nuts[start]
                nuts[start] = nuts[right]
                nuts[right] = tmp
                return right
        sortHelper(0, len(nuts)-1, True) #!!!!!!!!!!len(nuts)-1
        sortHelper(0, len(bolts)-1, False) #!!!!!!!len(bolts)-1
        return
