class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       list_sum=[]
       for i in range(len(nums)):
          for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                list_sum.append(i)
                list_sum.append(j)
       return list_sum         