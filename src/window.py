from tkinter import Tk, BOTH, Canvas, Button
from __main__ import *
import time

# Creates graphical window for the maze.
class Window:
    # Window constructor
    def __init__(self, width, height, solve_maze):
        self.width = width
        self.solve_maze = solve_maze
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.button = Button(self.root, text="Solve", command=self.on_button_clicked)
        self.running = False
        self.canvas.pack()
        self.button.pack(pady=20)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # Updates the idle pending tasks
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    # This will continuously call redraw until window gets closed
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            time.sleep(0.05)

    # This closes the window
    def close(self):
        self.running = False

    def on_button_clicked(self):
        self.solve_maze()

    # calls a instance of Line to create a line on the canvas.
    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.canvas, fill_color)

# Allows for points to be specified.
class Point:
    # Point Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

# For drawing lines.
class Line:
    # Line Constructor
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    # Uses points from point class to create a line. 
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


