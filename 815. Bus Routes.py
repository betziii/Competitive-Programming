class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(bus)
        q = deque([(source, 0)])
        stopvisit, busvisit = set(), set()
        while q:
            stop, res = q.popleft()
            if stop == target:
                return res
            for bus in graph[stop]:
                if bus not in busvisit:
                    busvisit.add(bus)
                    for stop in routes[bus]:
                        if stop not in stopvisit:
                            stopvisit.add(stop)
                            q.append((stop, res + 1))
        return -1
            
