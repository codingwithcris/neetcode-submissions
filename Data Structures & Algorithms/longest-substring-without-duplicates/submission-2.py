class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_substring = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                max_substring = max(len(seen), max_substring)
            else:
                seen.remove(s[l])
                l += 1

        return max_substring
