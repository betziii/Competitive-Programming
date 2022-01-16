class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dicts = {}
        res  = []
        for i in nums2:
            if len(stack) == 0:
                stack.append(i)
            elif i > stack[-1]:
                while len(stack) > 0 and i > stack[-1] :
                    dicts[stack.pop()] = i
                stack.append(i)
            else:
                stack.append(i)
            
        for n in nums1:
            if n in dicts:
                res.append(dicts[n])
            else:
                res.append(-1)
        return res            
            
            