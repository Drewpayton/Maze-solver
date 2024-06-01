from window import *

if __name__ == "__main__":
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line, "black")
    win.wait_for_close()