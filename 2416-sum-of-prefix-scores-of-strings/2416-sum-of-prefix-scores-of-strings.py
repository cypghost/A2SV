class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        count_dict = {}
        
        for word in words:
            st = ""
            
            for char in word:
                st += char
                
                if st in count_dict:
                    count_dict[st] += 1
                
                else:
                    count_dict[st] = 1
        
        ans = []
        
        for word in words:
            st = ""
            count = 0
            
            for char in word:
                st += char
                count += count_dict[st]
            
            ans.append(count)
        
        return ans