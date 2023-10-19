class Solution:
    def countGoodNumbers(self, n: int) -> int:
#         MOD = int(1e9 + 7)
        
#         def recursion(a, sums):
#             if a == n + 1:
#                 return sums
            
#             if a != 1 and a % 2 != 0:
#                 sums *= 5

#             if a % 2 == 0:
#                 sums *= 4

#             return recursion(a + 1, sums % MOD)
        
#         sums = 5
#         res = recursion(1, sums)
#         return res % MOD

            Mod = 10**9 + 7
            
            def myPow(x: int, n: int, mod: int) -> int:                
                if n == 0:
                    return 1

                elif n == 1:
                    return x

                else:
                    half = myPow(x, n // 2, mod)

                    if n % 2 == 0:
                        return (half * half) % mod
                  
                return ((half * half) % mod * x) % mod

            if n % 2 == 0:
                return ((myPow(4, n // 2, Mod)) * (myPow(5, n // 2, Mod))) % (Mod)
            
            return ((myPow(4, n // 2, Mod) * (myPow(5, 1 + n // 2, Mod)))) % (Mod)