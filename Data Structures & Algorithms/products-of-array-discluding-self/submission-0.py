class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = len(nums)
        res= [0]*num

        for i in range(num):
            prod=1
            for j in range(num):
                if i==j:
                    continue
                prod *=nums[j]
            res[i]=prod
        return res               