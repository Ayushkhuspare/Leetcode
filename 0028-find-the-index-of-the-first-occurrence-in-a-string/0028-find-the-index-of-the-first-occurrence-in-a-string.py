class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
        # for i in range(len(haystack)) and range(len(needle)):
        #     if haystack[i] == needle[i]:
        #         return 0
        #     else:
        #         return -1    


        