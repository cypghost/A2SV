class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = [[] for index in range(2)]
        
        # stores the count of losses a player has
        losses = Counter()
        
        # stores value 0 if no losses, and if value 1 with only one loss
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            
            losses[loser] += 1
        
        # append the winner with 0 to answer[0] and with loss 1 to answer[1]
        for player, numloss in losses.items():
            if numloss < 2:
                answer[numloss].append(player)
            
        # returns the sorted form of the array 
        return [sorted(answer[0]), sorted(answer[1])]
            
         
        
        

                    
    