import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from cubic import Cubic
from calculations import Calculations

class main:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Points Plotter")
        self.window.geometry("1200x800")

        self.x1Entry = tk.Entry(self.window)
        self.y1Entry = tk.Entry(self.window)
        self.x2Entry = tk.Entry(self.window)
        self.y2Entry = tk.Entry(self.window)

        self.x1Entry.pack()
        self.y1Entry.pack()
        self.x2Entry.pack()
        self.y2Entry.pack()

        self.x1Entry.bind("<Return>",self.Input)
        self.x2Entry.bind("<Return>",self.Input)
        self.y1Entry.bind("<Return>",self.Input)
        self.y2Entry.bind("<Return>",self.Input)
        
        self.CreateGraph()

        self.window.mainloop()

    def CreateGraph(self):

        self.figure = plt.figure(figsize=(12,6))
        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # init values
        self.x1Axis = 0
        self.x2Axis = 10
        self.y1Axis = 0
        self.y2Axis = 10

        self.Cubic = Cubic(0,0,0,0)
        self.Calc = Calculations()

        self.PlottedPoints = []
        self.Spline = None

        self.axis.set_xlim(self.x1Axis, self.x2Axis)
        self.axis.set_ylim(self.y1Axis, self.y2Axis)

        self.canvas.mpl_connect("button_press_event", self.OnClick)

    def UpdateGraph(self):

        self.axis.set_xlim(self.x1Axis, self.x2Axis)
        self.axis.set_ylim(self.y1Axis, self.y2Axis)

        self.canvas.draw()

    def SplineFunction(self):

        if self.Spline is not None:
            self.Spline.remove()

        RightSide, LeftSide = self.Calc.GetEquations(self.PlottedPoints)
        Equations = self.Calc.MergeSides(RightSide, LeftSide)
        Derivative = self.Calc.SolveEquations(Equations)
        Coefficients = self.Calc.GetCoefficients(self.PlottedPoints, Derivative)
        XValues, YValues = self.Cubic.GetSplinePoints(self.PlottedPoints, Coefficients)

        self.Spline = self.axis.plot(XValues, YValues)[0]

    def OnClick(self, click):

        if click.inaxes != self.axis: return

        self.axis.plot(click.xdata, click.ydata, "x")

        self.PlottedPoints.append([click.xdata, click.ydata])
        self.PlottedPoints.sort(key=lambda point: point[0])

        if len(self.PlottedPoints) >= 2:
            self.SplineFunction()

        self.UpdateGraph()


    # X and y axis inputs
    def Input(self, event):

        self.x1Axis = float(self.x1Entry.get())
        self.x2Axis = float(self.x2Entry.get())
        self.y1Axis = float(self.y1Entry.get())
        self.y2Axis = float(self.y2Entry.get())

        self.UpdateGraph()




run = main()