class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash = {nums[i]:i}
        hash = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash :
                #si on a déja croisé le bon complément on va le chercher en O(1)
                return [hash[diff], i]
            else:
                hash[num] = i