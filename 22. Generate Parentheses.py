class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        my_list = []
        def helper(string, op, close):
            if len(string) == 2 * n:
                my_list.append(string)
            if op < n:
                helper(string+"(", op + 1, close)
            if close < n and op > close:
                helper(string+")", op, close + 1)
        helper("", 0, 0)
        return my_list
