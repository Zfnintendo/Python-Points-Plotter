import numpy as np

class Cubic: 

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def EvaluateCubic(self, Coefficients, x, xStart):

        a, b, c, d = Coefficients

        LocalX = x - xStart

        return a * LocalX**3 + b * LocalX**2 + c * LocalX + d

    def GetSplinePoints(self, arr, Coefficients):

        XValues = []
        YValues = []

        for i in range(len(Coefficients)):

            xStart = arr[i][0]
            xEnd = arr[i+1][0]

            XSection = np.linspace(xStart, xEnd, 50)

            for x in XSection:

                y = self.EvaluateCubic(Coefficients[i], x, xStart)

                XValues.append(x)
                YValues.append(y)

        return XValues, YValues
    