class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        # get accummulate sum of col values
        # passed with minor defects, need to remember the basic 'find_zero()' function
        # need to use zip(list, list) function for consiced python matrix manipulation
        # algorithm come from lecture, need to think myself
        def find_zero():
            totSum = 0
            dic = {0: -1}
            for i in xrange(len(tmp_array)):
                totSum += tmp_array[i]
                if totSum in dic.keys():
                    return [dic[totSum]+1, i]
                dic[totSum] = i
            return [None, None]
        m = len(matrix)
        n = len(matrix[0])
        accu_col = [[0 for i in xrange(n)] for j in xrange(m+1)]
        for i in xrange(m):
            accu_col[i+1] = [a+b for a, b in zip(accu_col[i], matrix[i])] ## use of zip 
        tmp_array = [0 for i in xrange(n)]
        for start_row in xrange(m):
            for end_row in xrange(start_row, m):
                tmp_array = [a-b for a, b in zip(accu_col[end_row+1], accu_col[start_row])] # use of zip
                start_col, end_col = find_zero()
                if start_col is not None: #!!! not if start_col, because start_col still valid for start_col == 0 case!!!!
                    return [[start_row, start_col], [end_row, end_col]]
        return None
