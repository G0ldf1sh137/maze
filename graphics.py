from tkinter import Tk, BOTH, Canvas


class Window:
    
    def __init__(self, width=800, height=600):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
            
    def close(self):
        self.running = False