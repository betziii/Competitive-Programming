import collections
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        
        activities = {}
        for log in logs:
            if log[0] not in activities:
                activities[log[0]] = set()
            activities[log[0]].add(log[1])
        
        for id, activity in activities.items():
            res[len(activity) - 1] += 1
        
        return res
