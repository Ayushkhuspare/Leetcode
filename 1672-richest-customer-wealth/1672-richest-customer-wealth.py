class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customers=[]
        for row in accounts:
            customers.append(sum(row))
        return max(customers)    
        