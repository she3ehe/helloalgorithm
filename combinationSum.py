class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        a = list(set(candidates))
        result = []
        self.helper(a,len(candidates),[],result,0,target)
        return result


    def helper(self,candidates,length,solution,result,pos,target):
        if(target < 0 or pos >= length):
            return
        elif(target > 0):
            for x in range(pos,length):
                solution.append(candidates[x])
                self.helper(candidates,length,solution,result,x,target-candidates[x])
                solution.pop()
        else:
            result.append([] + solution)