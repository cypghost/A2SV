class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        n = len(salary)
        
        small = 0
        add = 0
        
        if n == 3:
            return salary[n//2]
        
        elif n < 3:
            return 0
        
        while(small < (n-2)):
            add += salary[small + 1]
            small += 1
        add = add/small
        
        return add