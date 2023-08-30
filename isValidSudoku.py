class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash={}
        col_hash={}
        box_hash={}
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if i not in row_hash:
                        row_hash[i]=set()
                    if j not in col_hash:
                        col_hash[j]=set()
                    if (i//3,j//3) not in box_hash:
                        box_hash[(i//3,j//3)]=set()
                    if (board[i][j] in row_hash[i]) or (board[i][j] in col_hash[j]) or (board[i][j] in box_hash[(i//3,j//3)]):
                        return False
                    row_hash[i].add(board[i][j])
                    col_hash[j].add(board[i][j])
                    box_hash[(i//3,j//3)].add(board[i][j])
        
        return True