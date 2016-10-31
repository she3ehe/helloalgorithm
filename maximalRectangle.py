class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if(not matrix):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        sum = 0
        t = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == '0'):
                    t[i][j] = 0
                else:
                    t[i][j] = 1 if i == 0 else t[i-1][j] + 1
        for i in range(m):
            sum = max(sum,self.largestRectangleArea(t[i]))
        return sum

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        i = 0
        sum = 0
        while(i < len(heights)):
            if(not stack or heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                t = stack[-1]
                stack.pop()
                s = i if not stack else  i -stack[-1]- 1
                sum = max(sum,heights[t]*s)
        return sum

if __name__ == "__main__":
    print(Solution().maximalRectangle(["10100","10111","11111","10010"]))