class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first =0 
        for second in range(len(nums)):
            if nums[second] != val:
                
                nums[first],nums[second]=nums[second],nums[first]
                first+=1
        return first    

        