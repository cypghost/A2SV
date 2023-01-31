class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        '''
        (players., trainers)
        
        (4, 8), (4, 5), (4,8)
        (7,8), (7,8)
        (9, )
        '''
      # Approach 1  
#         players.sort()
#         trainers.sort()
        
#         right = len(trainers) - 1
#         left = 0
#         count = 0
        
#         while left < len(players) and right > -1:
#             if players[left] <= trainers[right]:
#                 right -= 1
#                 left += 1
#                 count += 1
#             else: 
#                 break
#         return count
    
    # Approcah 2
    
#         playptr = 0
#         trainptr = 0
#         count = 0
        
#         while playptr < len(players) and trainptr < len(trainers):
            
            
#             if players[playptr] > trainers[trainptr]:
#                 trainptr += 1
#                 continue
                
#             else:
#                 count += 1
#                 playptr += 1
#                 trainptr += 1
       # Approach 3
        
        ptr1 = len(players) - 1
        ptr2 = len(trainers) - 1
        count = 0
        
        players.sort()
        trainers.sort()
        
        while ptr1 > -1 and ptr2 > -1:
            
            if players[ptr1] > trainers[ptr2]:
                ptr1 -= 1
            
            else:
                ptr1 -= 1
                ptr2 -= 1
                count += 1
        
        
        return count