from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for _str in strs:
            anagram_dict[tuple(sorted(_str))].append(_str)
        return list(anagram_dict.values())
