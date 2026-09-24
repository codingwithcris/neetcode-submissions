class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked: list[int] = []

        for num in nums:
            if num in checked:
                return True
            else:
                checked.append(num)
            
        return False
            

        
