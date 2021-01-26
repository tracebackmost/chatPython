from tkinter import *
from tkinter.scrolledtext import ScrolledText


class GuiOutput:
    font = ('courier', 15, 'bold')

    def __init__(self, parent, width, height):
        self.width = width
        self.height = height
        self.parent = parent
        self.txt = None
        if parent:
            self.popupnow(parent)

    def popupnow(self, parent):
        if self.txt: return
        self.txt = ScrolledText(parent)
        self.txt.config(font=self.font, height=self.height, width=self.width)
        self.txt.pack(side=TOP)

    def write(self, text):
        self.popupnow(self.parent)
        self.txt.config(state=NORMAL)
        self.txt.insert(END, str(text))
        self.txt.see(END)
        self.txt.update()
        self.txt.config(state=DISABLED)

    def writelines(self, lines):
        for line in lines: self.write(line)

    def flush(self):
        pass
