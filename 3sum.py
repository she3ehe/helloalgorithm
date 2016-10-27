class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        ret = []
        for x in range(length - 2):
            i = x + 1
            j = length - 1
            while(i < j):
                if(nums[x] + nums[i] + nums[j] > 0 ):
                    j -= 1
                elif(nums[x] + nums[i] + nums[j] <0):
                    i += 1
                else:
                    if(not ret.__contains__([nums[x],nums[i],nums[j]])):
                       ret.append([nums[x],nums[i],nums[j]])
                    i += 1
        return ret