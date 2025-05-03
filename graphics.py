from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def __str__(self):
        return f"Point({self.x}, {self.y})"




class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        
        
    def __str__(self):
        return f"Line({self.p1}, {self.p2})"
    
    
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)




class Window:
    
    def __init__(self, width=800, height=600):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        
        
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
            
    def close(self):
        self.running = False