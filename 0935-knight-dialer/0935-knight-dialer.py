class Solution:
    def knightDialer(self, n: int) -> int:
        places = {
            0 : [6, 4],
            1 : [6, 8],
            2 : [9, 7],
            3 : [4, 8],
            4 : [0, 9, 3],
            5 : [],
            6 : [0, 7, 1],
            7 : [6, 2],
            8 : [3, 1],
            9 : [4, 2]
        }

        mod = 1e9 + 7

        @cache
        def dp(num, l):
            if l == 0:
                return 1

            ans = 0

            for i in places[num]:
                ans = (ans + dp(i, l - 1)) % mod

            return ans

        res = 0
        
        for i in range(10):
            res = (res + dp(i, n - 1)) % mod

        return int(res)