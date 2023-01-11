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
        k -= 1
        
        for index in range(n - 1):
            curr += k 
            curr %= n
            players.remove(players[curr])
            n -= 1 
        
        return players[0]
        
        # First 2 case Accepted code
        # m = n - k
        # return m