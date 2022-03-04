"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        summ = 0
        dicts = {}
        for i in employees:
            dicts[i.id]=i
        
        
        def summation(employee): #dfs
            nonlocal summ
            if not employee:
                return 0
            for i in employee.subordinates:
                summation(dicts[i])
            summ += employee.importance
        summation(dicts[id])
        return summ     