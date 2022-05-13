class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        dif = float('inf')
        T = 24*60
        
        for i in range(0, len(timePoints)): 
            a = timePoints[i-1].split(':')
            b = timePoints[i].split(':')
            
            c = abs(( int(a[0])- int(b[0]) )*60 + (int(a[1])- int(b[1]) ))
			
            c = c if c < T - c else T - c
            dif = c if c < dif else dif
			
            if not dif:
                return 0
            
        return dif