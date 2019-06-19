class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
    
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def solve(self):
        row, col = self.findUnassigned()
        #no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
            
    def isSafe(self, row, col, ch):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True

        

class BestSolution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def get_related_cells(target_cell):
            target_grid_index = target_cell[0] // 3 * 3 + target_cell[1] // 3
            # Return all related unsolved cells.
            related_cells = []
            for cell in self.unsolved_cells:
                grid_index = cell[0] // 3 * 3 + cell[1] // 3
                if cell[0] == target_cell[0] or cell[1] == target_cell[1] or grid_index == target_grid_index:
                    related_cells.append(cell)
            return related_cells
        
        def get_unique_solution(cell):
            # Return the unique solution if the cell has only one candidate, otherwise return None.
            if len(self.candidates[cell[0]][cell[1]]) == 1:
                return list(self.candidates[cell[0]][cell[1]])[0]
            else:
                return None
        
        def update_candidates(cell, value):
            changed_candidates = []
            
            # Update the cell.
            if cell in self.unsolved_cells:
                self.board[cell[0]][cell[1]] = value
                self.unsolved_cells.remove(cell)
            
            # Disable all other candidates for that cell.
            for digit in self.digits:
                if digit in self.candidates[cell[0]][cell[1]] and digit != value:
                    self.candidates[cell[0]][cell[1]].remove(digit)
                    changed_candidates.append((cell, digit))
            
            # Update all the related candidates.
            related_cells = get_related_cells(cell)
            for other_cell in related_cells:
                if value in self.candidates[other_cell[0]][other_cell[1]]:
                    self.candidates[other_cell[0]][other_cell[1]].remove(value)
                    changed_candidates.append((other_cell, value))
            
            return changed_candidates
        
        def rollback(updated_cells, updated_candidates):
            # Undo updates.
            for cell in updated_cells:
                self.unsolved_cells.add(cell)
                self.board[cell[0]][cell[1]] = "."
            for (cell, value) in updated_candidates:
                self.candidates[cell[0]][cell[1]].add(value)
        
        def _solveSudoku(updated_cells = [], updated_candidates = []):
            while len(self.unsolved_cells) > 0:
                # Check validality.
                for cell in self.unsolved_cells:
                    if len(self.candidates[cell[0]][cell[1]]) == 0:
                        # No possible solutions.
                        rollback(updated_cells, updated_candidates)
                        return False
                
                list_unsolved_cells = list(self.unsolved_cells)
                for cell in list_unsolved_cells:
                    value = get_unique_solution(cell)
                    if value is not None:
                        # Update all candidates with unique solution.
                        updated_cells.append(cell)
                        delta_updated_candidates = update_candidates(cell, value)
                        updated_candidates += delta_updated_candidates
                if len(self.unsolved_cells) == len(list_unsolved_cells):
                    break
            
            if len(self.unsolved_cells) > 0:
                # Need to form a guess.
                cell = min(self.unsolved_cells, key = lambda cell: len(self.candidates[cell[0]][cell[1]]))
                for value in self.candidates[cell[0]][cell[1]]:
                    initial_updated_cells = [cell]
                    initial_updated_candidates = update_candidates(cell, value)
                    
                    is_solved = _solveSudoku(initial_updated_cells, initial_updated_candidates)
                    if is_solved:
                        return True
                
                # No solution found after iterating all possible candidates of a given cell.
                rollback(updated_cells, updated_candidates)
                return False
            else:
                return True
        
        self.board = board
        self.digits = "123456789"
        self.unsolved_cells = set([(i, j) for i in range(9) for j in range(9) if self.board[i][j] == "."])
        self.candidates = [[set(self.digits) for _ in range(9)] for _ in range(9)]
        
        # Initialize all candidates.
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != ".":
                    update_candidates((i, j), value)
        
        _solveSudoku()