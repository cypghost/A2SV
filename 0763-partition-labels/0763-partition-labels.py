class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = len(s)
        
        # last appearance of the letter
        last = {s[index]: index for index in range(size)} 
        
        idx = 0
        ans = []
        
        while idx < size:
            
            end = last[s[idx]]
            itr = idx + 1
            
            # validation of the part [idx, end]
            while itr < end:
                if last[s[itr]] > end:
                    # extend the part
                    end = last[s[itr]] 
                
                itr += 1
           
            ans.append(end - idx + 1)
            idx = end + 1
            
        return ans