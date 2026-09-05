class Cubic: 

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def AnswerOnInput(self, x):
        return self.a*x**3 + self.b*x**2 + self.c*x + self.d

    
    