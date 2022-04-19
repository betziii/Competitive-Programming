class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        child = [1]* n
        
        m = len(accounts[0])
        def findParent(node):
            if node != parent[node]:
                parent[node] = findParent(parent[node])
            return parent[node]
        def union(node1, node2):
            p1, p2 = findParent(node1), findParent(node2)
            if p1 != p2:
                p1, p2 = sorted([p1, p2], key = lambda x:child[x])
                parent[p1] = p2
                child[p2] += child[p1]
        
        emailname = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailname:
                    emailname[email] = i
                else:
                    union(i, emailname[email])
        component = defaultdict(set)
        for email in emailname.keys():
            component[findParent(emailname[email])].add(email)
            
        ans = []
        for k, v in component.items():
            ans.append([accounts[k][0]] + sorted(list(v)))
        return ans
                    
                    
                    
                    
        