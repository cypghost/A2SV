class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        players = [index for index in range(1, n + 1)]
        curr = 0
        friendsleft = n
        
        for index in range(n - 1):
            curr = (curr + k - 1) %  friendsleft
            players.remove(players[curr])
            friendsleft -= 1 
        
        return players[0]
        