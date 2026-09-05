class Calculations:

    # array has to be a 2d matrix with 2 elements in each row
    def GetPointsDistance(self, arr, axis):
        Distances = []

        for i in range(len(arr) - 1):
            Distances.append(arr[i+1][axis] - arr[i][axis])

        return Distances

    def GetSlopes(self, arr):
        slopes = []
        yDiffs = self.GetPointsDistance(arr, 1)
        xDiffs = self.GetPointsDistance(arr, 0)

        for i in range(len(yDiffs)):
            slopes.append(yDiffs[i]/xDiffs[i])

        return slopes

    def GetEquations(self, arr):
        Distances = self.GetPointsDistance(arr, 0) 
        Slopes  = self.GetSlopes(arr)

        RightSide = []
        LeftSide = []

        for i in range(1, len(arr) - 1):

            # Right side
            RightSide.append(6 * (Slopes[i] - Slopes[i-1]))

            # left side
            row = [0] * (len(arr) - 2)

            LeftCoefficient1 = Distances[i-1]
            LeftCoefficient2 = 2 * (Distances[i-1] + Distances[i])
            LeftCoefficient3 = Distances[i]

            # Put the coefficients in their correct positions
            if i > 1:
                row[i-2] = LeftCoefficient1

            row[i-1] = LeftCoefficient2

            if i < len(arr) - 2:
                row[i] = LeftCoefficient3

            LeftSide.append(row)

        return RightSide, LeftSide

    def MergeSides(self, RightSide, LeftSide):
        Equations = []
        
        for i in range(len(LeftSide)):
            Equations.append(LeftSide[i] + [RightSide[i]])

        return Equations


