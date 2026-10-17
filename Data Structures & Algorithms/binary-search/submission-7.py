class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)
        
    def binary_search(self, nums: List[int], target: int, l: int, h: int) -> int:
        if l > h:
            return -1
        
        mid: int = l + ((h-l) // 2)

        if nums[mid] > target:
            return self.binary_search(nums, target, l, mid-1)
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid+1, h)
        else:
            return mid