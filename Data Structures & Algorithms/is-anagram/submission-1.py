class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_trie=sorted(s)
        t_trie=sorted(t)
        return s_trie==t_trie