class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0 
        
        unique = sorted(set(nums))
        print(unique)
        number_current = 1
        number_streak = 1 
        for i in range(1,len(unique)):
            if unique[i] -1 == unique[i-1] :
                number_current +=1
            else :
                number_streak = max(number_streak, number_current)
                number_current = 1    
        return max(number_current, number_streak)             
        