class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        add = 0
        
        while tickets[k] != 0:
            for front in range(n):
                if tickets[k] == 0:
                    break
                
                if tickets[front] != 0:
                    add += 1
                    tickets[front] -= 1 
            
        return add
            