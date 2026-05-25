class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       trie={}
       for i in nums :
         if i in trie:
            trie[i] +=1
         else :
            trie[i] = 1
       return sorted(trie, key=trie.get , reverse = True)[:k]   