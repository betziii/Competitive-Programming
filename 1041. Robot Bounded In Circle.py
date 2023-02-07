class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        d = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in instructions:
          if i == 'G':
            x += directions[d][0]
            y += directions[d][1]
          elif i == 'L':
            d = (d + 3) % 4
          else:
            d = (d + 1) % 4

        return (x, y) == (0, 0) or d > 0
