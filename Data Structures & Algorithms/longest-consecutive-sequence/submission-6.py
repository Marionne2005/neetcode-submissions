class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       if len(nums)==0:
          return 0
       element=set(nums)   
       current=1
       for i in element:
          current_element=1
          if  i+1 in element:
            while current_element+i in element:
              current_element +=1
          current=max(current,current_element)
       return current            