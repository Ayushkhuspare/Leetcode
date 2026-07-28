class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentstreak=0
        maxstreak=0
        for num in nums:
            if num==1:
                currentstreak+=1
            else:
                 
                 currentstreak = 0
            maxstreak = max(maxstreak, currentstreak)     
        return maxstreak    
       
           

        