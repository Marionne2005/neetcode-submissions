class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       nums_trie=sorted(nums)
       trie={}
       for i in nums_trie :
         if i in trie:
            trie[i] +=1
         else :
            trie[i] = 1
       result = []
       list_trie= sorted(trie, key=trie.get, reverse=True)
       for i in range(k):
         result.append(list_trie[i])
       return result   