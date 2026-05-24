class  Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums=set(nums)
        return not(nums==list(set_nums))