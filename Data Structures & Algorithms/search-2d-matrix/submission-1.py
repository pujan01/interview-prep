class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        h = m*n - 1
        while l <= h:
            mid = (l + h ) // 2
            if self.matrixVal(m,n,matrix, mid) == target:
                return True
            elif self.matrixVal(m,n,matrix, mid) > target:
                h = mid - 1
            else:
                l = mid + 1
        return False

    def matrixVal(self, m, n, matrix, k):
        print(m, n, matrix, k)
        quotient, remainder = divmod(k, n)
        return matrix[quotient][remainder]

