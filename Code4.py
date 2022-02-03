class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #print()
        richest=0
        for i in range(len(accounts)):
            #richest=0
            wealth=0            
            for j in range(len(accounts[i])):
                wealth=wealth + accounts[i][j]
                j=j+1
            if wealth> richest:
                richest=wealth
            i=i+1
        return richest
---------------------------------------------------------------------------------
// one liner
