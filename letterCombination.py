from collections import deque
class Solution(object):
    m = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if(not digits):
            return result
        str = []
        self.helper(digits,str,result)
        return result

    def helper(self,digits,solution,result):
        if(not digits):
            result.append("".join(solution))
            return
        for x in self.m[digits[0]]:
            solution.append(x)
            self.helper(digits[1:],solution,result)
            solution.pop()