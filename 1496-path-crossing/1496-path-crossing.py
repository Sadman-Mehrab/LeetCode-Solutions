class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()

        currentX, currentY = 0, 0

        points.add((currentX, currentY))

        for p in path:
            if p == 'N':
                currentY += 1
            elif p == 'S':
                currentY -= 1
            elif p == 'E':
                currentX += 1
            elif p == 'W':
                currentX -= 1

            if (currentX, currentY) in points:
                return True
            else:
                points.add((currentX, currentY))
        
        return False
