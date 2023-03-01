class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1 = "0"
        
        def invert (s1, count, n):
            
            if count == n:
                return s1
            
            else:
                arr = []
                
                for index in range(len(s1)):
                    if s1[index] =="1":
                        arr.append("0")
                    
                    else:
                        arr.append("1")
                
                return invert(s1 + "1" + "".join(arr[::-1]), count + 1, n)
            
        return invert(s1, 0, n)[k - 1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         s1 = "0"
#         s2 = "011"
                
#         def invert(s2):
#             if n == 1:
#                 return s1
            
#             else:
#                 s3 = ""
#                 s4 = ""
                    
#                 for index in range(len(s2)):
#                     if s2[index] == "1":
#                         s4 += "0"
                    
#                     else:
#                         s4 += "1"
                        
#                 s3 = s2 + "1" + s4[::-1]
                
#             return s3
         
#         for index in range(len(s2)):
#             s2 = invert(s2)
               
#         return s2[k-1]