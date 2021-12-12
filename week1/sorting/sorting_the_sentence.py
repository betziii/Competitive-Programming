class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = list(s.split(" "))
        strings1 = [0]*len(list1)
        for i in list1:
            strings1[int(i[-1])-1] = i[:-1]
        return " ".join(strings1)