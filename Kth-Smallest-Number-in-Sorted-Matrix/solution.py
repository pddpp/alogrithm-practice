class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        # visited matrix will lead to ETL if matrix is too large, so optimal solution is to use min of k and len(matrix) for the size of visited
        # idea got myself, easy heap question with minor defects
        import heapq
        if not matrix or not matrix[0] or k > len(matrix)*len(matrix[0]):
            return None
        len_col = min(k, len(matrix[0]))
        len_row = min(k, len(matrix))
        visited = [[False for i in xrange(len_col)] for j in xrange(len_row)]
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0)) # !!!!!!!!!heappush() and heap pop(), not push() or pop()
        visited[0][0] = True
        for i in xrange(k):
            val, x, y = heapq.heappop(heap)
            if x+1 < len(visited) and not visited[x+1][y]: # use visited here
                heapq.heappush(heap, (matrix[x+1][y], x+1, y))
                visited[x+1][y] = True
            if y+1 < len(visited[0]) and not visited[x][y+1]: # use visited[0] here
                heapq.heappush(heap, (matrix[x][y+1], x, y+1))
                visited[x][y+1] = True
        return val
        
