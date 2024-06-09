from window import Point, Line
import time

# This will allow us to create multiple cells which can have anywhere from 0 - 4 walls 
class Cell:
    def __init__(self, win=None, visited=False):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    # This will draw the lines between the points
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Checks to see if any wall is false then draws the line between each point.
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line)
        else:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line, "white")

        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line)
        else:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line, "white")

        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line)
        else:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line, "white")

        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line)
        else:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line, "white")

    # Draws the move between each cell.
    def draw_move(self, to_cell, undo=False):
        # Gathers the center of the current cell
        self.center_x = (self._x1 + self._x2) // 2
        self.center_y = (self._y1 + self._y2) // 2 

        # Gathers the current center of the cell its going to.
        cell_center_x = (to_cell._x1 + to_cell._x2) // 2
        cell_center_y = (to_cell._y1 + to_cell._y2) // 2

        # draws the line between the two cells
        line = Line(Point(self.center_x, self.center_y), Point(cell_center_x, cell_center_y))
        if not undo:
            self._win.draw_line(line, fill_color="red")
        else:
            self._win.draw_line(line, fill_color="grey")

            
            