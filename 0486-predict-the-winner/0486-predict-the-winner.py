class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        start = 0
        end = len(nums) - 1
        p1_turn = True
        
        def winner(first, last, p1_turn):
            
            if first == last:
                
                return [nums[first], 0] if p1_turn else [0, nums[first]]
            
            if p1_turn:
                ans = winner(first + 1, last, False)
                ans[0] += nums[first]
                
                add = winner(first, last - 1, False)
                add[0] += nums[last]
                
                if ans[0] > add[0]:
                    return ans
                
                else:
                    return add
                
            else:
                ans1 = winner(first + 1, last, True)
                ans1[1] += nums[first]
                
                add1 = winner(first, last - 1, True)
                add1[1] += nums[last]
                      
                if ans1[1] > add1[1]:
                    return ans1
                
                else:
                    return add1
            
        ans =  winner(start, end, True) 
        
        return ans[0] >= ans[1]
            
            
            
            
            