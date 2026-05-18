class Solution:
    def addToSet(self, board, nums, i, j):
        if board[i][j] in nums:
                return False
        if board[i][j] != ".":
                nums.add(board[i][j])
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows 
        # 0 to 2, 3 to 6, 6 to 9
        
        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            if i % 3 == 0:
                r1 = set()
                r2 = set()
                r3 = set()
            for j in range(len(board[i])):
                if not self.addToSet(board, rowSet, i, j): return False
                if not self.addToSet(board, colSet, j, i): return False
                
                if 0 <= j < 3:
                    if not self.addToSet(board, r1, i, j): return False
                if 2 < j < 6:
                    if not self.addToSet(board, r2, i, j): return False
                if 5 < j < 9:
                    if not self.addToSet(board, r3, i, j): return False
                
        return True

    