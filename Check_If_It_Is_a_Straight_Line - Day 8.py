def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
         if len(coordinates)==2:
            return True
         for i in range(2,len(coordinates)):
            y3 = coordinates[i-2][1]
            y2 = coordinates[i-1][1]
            y1 = coordinates[i][1]
            x3 = coordinates[i-2][0]
            x2 = coordinates[i-1][0]
            x1 = coordinates[i][0]
            if((y3 - y2)*(x2 - x1) != (y2 - y1)*(x3 - x2)):
                return False
            return True