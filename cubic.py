class Cubic: 

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def AnswerY(self, x):
        return self.a*x**3 + self.b*x**2 + self.c*x + self.d

    def EvaluateCubic(self, Coefficients, xEnd, xStart):

        a, b, c, d = Coefficients

        LocalX = xEnd - xStart

        return a * LocalX**3 + b * LocalX**2 + c * LocalX + d
    
    