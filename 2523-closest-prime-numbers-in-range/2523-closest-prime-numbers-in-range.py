class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_primenumber(num):
            for index in range(2, int(num ** 0.5) + 1):
                if num % index == 0:
                    
                    return False
            
            return True
        
        
        prime = []
        
        if left % 2 == 0 or left == 1:
            left += 1
            
        if left == 2:
            prime.append(left)
            left += 1
        
        for num in range(left, right + 1, 2):
            if is_primenumber(num):
                if prime and num <= prime[-1] + 2:
                    
                    return [prime[-1], num]
                
                prime.append(num)
                      
        if len(prime) <= 1:
            return [-1, -1]
    
        elif prime[1] - prime[0] <= prime[-1] - prime[-2]:
            return [prime[0], prime[1]]
        
        else:
            return [prime[-2], prime[-1]]
        
        
        