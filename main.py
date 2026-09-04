import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class main:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Points Plotter")
        self.window.geometry("1200x800")

        self.xEntry = tk.Entry(self.window)
        self.yEntry = tk.Entry(self.window)

        self.xEntry.pack()
        self.yEntry.pack()

