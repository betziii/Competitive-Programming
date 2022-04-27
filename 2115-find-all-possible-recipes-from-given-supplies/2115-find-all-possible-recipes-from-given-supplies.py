class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)
        ans = []
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
            
            indegree[recipes[i]] = len(ingredients[i])
                
        
        q = deque(supplies)
        while q:
            supply = q.popleft()
            for val in graph[supply]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        
        for k,v in indegree.items():
            if v == 0:
                ans.append(k)
        return ans
