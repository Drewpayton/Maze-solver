from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk.Tk()
        self.root.title("Tkinter Project")
        self.canvas = Canvas(self.root, self.width, self.height, bg="yellow")
        self.running = False
        self.canvas.pack()