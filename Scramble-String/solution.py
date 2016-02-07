class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    # Idea got from lecture and coded myself with one defect.
    def isScramble(self, s1, s2):
        # Write your code here
        if len(s1) == 1 and len(s2) == 1:
            return s1 == s2
        s1_sorted = ''.join(sorted(s1)) # Sort letters in string
        s2_sorted = ''.join(sorted(s2))
        if not s1_sorted == s2_sorted:
            return False
        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): #!!!!!!!!need "self."
                return True
            if self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]):
                return True
        return False
