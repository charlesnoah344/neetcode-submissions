class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seq = set(nums)
        return len(seq) != len(nums)
        