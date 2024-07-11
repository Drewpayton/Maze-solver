from cell import Cell
from window import *
import time
import random

class Maze:

    # Maze constructor
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()
        

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            placeHolder = []
            if i > 0 and not self._cells[i - 1][j].visited:
                placeHolder.append((i-1, j))

            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                placeHolder.append((i+1, j))
            
            if j > 0 and not self._cells[i][j-1].visited:
                placeHolder.append((i, j-1))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                placeHolder.append((i, j+1))
            
            if len(placeHolder) == 0:
                self._draw_cell(i, j)
                return 
            
            direction_index = random.randrange(len(placeHolder))
            next_index = placeHolder[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
           
        

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False 

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        if (i,j) == (self.num_cols - 1, self.num_rows - 1):
            return True
    
        self._animate()
        self._cells[i][j].visited = True

        if j > 0 and self._cells[i][j].has_top_wall == False:
            if self._cells[i][j-1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        if j < self.num_cols - 1 and self._cells[i][j].has_bottom_wall == False:
            if self._cells[i][j+1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        if i > 0 and self._cells[i][j].has_left_wall == False:
            if self._cells[i-1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        
        if i < self.num_cols - 1 and self._cells[i][j].has_right_wall == False:
            if self._cells[i+1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

        

        return False

