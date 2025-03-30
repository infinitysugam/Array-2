class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        change_map0 = []
        change_map1 = []

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                result = sum(self.getneighbourindex(board,i,j))
                if board[i][j]==1 and (result < 2 or  result > 3):
                    change_map0.append([i,j])
                if board[i][j]==1 and result in [2,3]:
                    change_map1.append([i,j])

                if board[i][j]==0 and result ==3:
                    change_map1.append([i,j])
                

        for i,j in change_map0:
            board[i][j]=0
        for i,j in change_map1:
            board[i][j]=1
        

    

    def getneighbourindex(self,board,i,j):
        
        initial_state = []
        if i!=0:
            initial_state.append(board[i-1][j])
            if j!=len(board[0])-1:
                initial_state.append(board[i-1][j+1])
            if j!=0:
                initial_state.append(board[i-1][j-1])
        
        if j!=0:
            initial_state.append(board[i][j-1])
        if j!=len(board[0])-1:
            initial_state.append(board[i][j+1])

        if i!=len(board)-1:
            initial_state.append(board[i+1][j])

            if j!=0:
                initial_state.append(board[i+1][j-1])
            
            if j!=len(board[0])-1:
                initial_state.append(board[i+1][j+1])

        return initial_state

    
    



        