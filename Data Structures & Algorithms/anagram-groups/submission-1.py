from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for s in strs:
            k: list[str] = sorted(s)
            a[''.join(k)].append(s)        
                
        return [v for v in a.values()]