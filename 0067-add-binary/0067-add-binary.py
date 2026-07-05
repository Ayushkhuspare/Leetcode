class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry =0
        result=[]
        while i>=0 or j >= 0 or carry:
            if i>=0 :
                digitA=int(a[i])
            else:
                digitA=0
            if j>=0 :
                digitB=int(b[j])
            else:
                digitB=0
            total = digitA + digitB + carry    
            result.append(str(total%2))   
            carry = total // 2
            i-=1
            j-=1
        return "".join(result[::-1] )                   


        