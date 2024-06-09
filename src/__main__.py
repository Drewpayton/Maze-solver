from window import *
from cell import Cell
from maze import Maze

if __name__ == "__main__":
    win = Window(800, 600)
    num_cols = 16
    num_rows = 12
    cell_size_x = (800 - 2 * 50) / num_cols
    cell_size_y = (600 - 2 * 50) / num_rows

    m1 = Maze(50, 50, num_rows, num_cols, cell_size_x, cell_size_y, win)

    m1.solve()
    win.wait_for_close()