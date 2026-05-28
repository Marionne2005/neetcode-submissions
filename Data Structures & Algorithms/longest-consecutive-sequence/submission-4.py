class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0 
        
        result = set (nums)
        current =1 
        for i in result :
          if i-1 not in result: 
            current_element=1
            while i+current_element in result:
              current_element +=1
            current=max(current,current_element)
        return current      