class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        if n > 0:
            ans[1] = 1
            
        for index in range(n + 1):
            if index % 2 == 0:
                ans[index] = ans[index // 2]
            
            else:
                ans[index] = ans[index // 2] + 1
            
        return ans
    
        # Solution 1
        
#         ans = []
        
#         for index in range(n + 1):
#             ans.append(index.bit_count())
        
#         return ans
    
        # Solution 2
        
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
        
        
                
            
