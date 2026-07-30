class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first= 1
        for second in range(1,len(nums)):
            if nums[second]!=nums[first-1]:
                nums[first],nums[second]=nums[second],nums[first]
                first += 1
        return first