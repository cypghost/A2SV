class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        lettert = {}
        # To find the element added to t
        for a in t:
            letters[a] = s.count(a)
            lettert[a] = t.count(a)
            if letters[a] != lettert[a]:
                return a 
            
        
                
           
                
           
        
        
        
        
        
        
        
            # if s[pointer1] == t[pointer1]:
            #    pointer1 += 1
                
            # else: 
            #    print(t[pointer1])
            #    break
          
        
        
        # for i in range(n):
        #  if s[i] != t[i]:
        #       print(t[i])
        #       break