class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = []
        
        left = 0
        right = len(skill) - 1
        
        add = skill[left] + skill[right]
        sums = 0
        
        while left < right:
            if skill[left]  + skill[right] == add:
                ans.append((skill[left], skill[right]))
            
            else:
                ans.append((skill[left], skill[right]))
                return -1
                
            sums += skill[right] * skill[left]
            
            left += 1
            right -= 1
            
        return sums
                
        
        