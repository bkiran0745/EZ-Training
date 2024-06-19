import ast
class Solution:
    def twoSum(self,nums,target):
        lis = []
        for i in range(0,len(nums)):
            for j in range(1,len(nums)-1):
                if nums[i]+nums[j] == target:
                    lis = [i,j]
                    return lis
nums = ast.literal_eval(input())
target = int(input())
x = Solution().twoSum(nums,target)
print(x)