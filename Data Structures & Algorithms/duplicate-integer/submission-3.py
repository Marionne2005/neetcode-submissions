class  Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums=set(nums)
        list_trie=list(set_nums)
        if list_trie == nums :
            return False
        else:    
            return True