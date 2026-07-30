class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        first =0
        for second in range(len(nums)):
            if nums[second] !=0:
                nums[first],nums[second]=nums[second],nums[first] 
                first+=1
               


            




        

        """
        Do not return anything, modify nums in-place instead.
        """
        