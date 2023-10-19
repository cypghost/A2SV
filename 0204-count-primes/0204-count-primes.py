class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n + 1)]

        if n <= 2:
            return 0

        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1
    
        count = 0

        for p in range(2, n):
            if prime[p]:
                count += 1
        
        return count

#         def isPrime(n) : 
#             if (n <= 1) : 
#                 return False

#             if (n <= 3) : 
#                 return True

#             if (n % 2 == 0 or n % 3 == 0) : 
#                 return False
        
#             i = 5
#             while(i * i <= n) : 
#                 if (n % i == 0 or n % (i + 2) == 0) : 
#                     return False
#                 i = i + 6
                
        
#             return True 