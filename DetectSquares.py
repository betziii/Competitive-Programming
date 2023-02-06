class DetectSquares:

    def __init__(self):
        self.countp = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.countp[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        result = 0
        i, j = point
        
        for x, y in self.points:
            if (abs(j - y) != abs(i - x)) or x == i or y == j:
                continue
            result += self.countp[(x, j)] * self.countp[(i, y)]
        return result
