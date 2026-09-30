from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for s in strs:
            k: str = ''.join(sorted(s))
            a[k].append(s) 

        return list(a.values())