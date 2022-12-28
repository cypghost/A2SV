class Solution:
    def average(self, salary: List[int]) -> float:
        # sort the salary
        salary.sort()
        
        small = 0
        add = 0
        
        if len(salary) == 3:
            return salary[len(salary)//2]
        
        elif len(salary) < 3:
            return 0
        
        while(small < (len(salary)-2)):
            add += salary[small + 1]
            small += 1
            
        add = add/small
        
        return add