from __future__ import annotations

from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y) -> Point:
        self.x = x
        self.y = y
        
        
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"




class Line:
    def __init__(self, p1: Point, p2: Point) -> Line:
        self.p1 = p1
        self.p2 = p2
        
        
    def __str__(self) -> str:
        return f"Line({self.p1}, {self.p2})"
    
    
    def draw(self, canvas: Canvas, fill_color: str = "black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)




class Window:
    
    def __init__(
        self, 
        width: int = 800,
        height: int = 600
    ) -> Window:
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        
        
    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.canvas, fill_color)

    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    
    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
            
            
    def close(self) -> None:
        self.running = False