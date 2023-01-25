class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        
        add = skill[left] + skill[right]
        
        sums = 0
        
        while left < right:
            if skill[left]  + skill[right] == add:
                sums += skill[right] * skill[left]
            
            else:
                return -1
                
            left += 1
            right -= 1
            
        return sums
                
        
        