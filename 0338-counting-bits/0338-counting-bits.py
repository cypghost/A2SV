class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for index in range(n + 1):
            ans.append(index.bit_count())
        
        return ans
        
#         ans = [0] * (n + 1)
        
#         def check(start):
#             temp = start
            
#             if temp >= len(ans):
#                 return ans
            
#             count = 0
            
#             if start == 1:
#                 ans[start] += 1
                
#             else:
#                 res = ""
#                 while start > 0:
#                     rem = start % 2
#                     res += str(rem)
#                     start = start // 2
                    
#                 ans[temp] += res.count("1")
                
#             check(temp + 1)
            
#         check(0)
        
#         return ans
        
        
                
            
