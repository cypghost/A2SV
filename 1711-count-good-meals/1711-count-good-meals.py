class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        Meals = {}
        count = 0
        
        for food in deliciousness:
            
            if len(Meals) == 0:
                Meals[food]=0
                
            for meal in range(22):
                if (2**meal) - food in Meals:
                    count += Meals[(2**meal) - food] 
                    
            if food not in Meals:
                Meals[food] = 1
                
            elif food in Meals or Meals[food] == 0:
                Meals[food] += 1  
                
        return count % ((10**9)+7)
        
        
        
            
    