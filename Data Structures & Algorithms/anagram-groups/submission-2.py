class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       dic_output={}
       for i in strs:
         key_trie=tuple(sorted(i))
         if key_trie not in dic_output:
            dic_output[key_trie]=[]
         dic_output[key_trie].append(i) 
       return list(dic_output.values())    
                 