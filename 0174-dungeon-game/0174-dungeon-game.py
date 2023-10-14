class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)
        c = len(dungeon[0])

        def possible(n):
            mat = [[-float("inf") for x in range(c)] for _ in range(r)]
            mat[0][0] = n + dungeon[0][0]

            for row in range(r):
                for col in range(c):
                    if row == 0 and col == 0:
                        continue

                    up, left = -float("inf"), -float("inf")

                    if row-1>=0:
                        up = mat[row-1][col]

                    if col-1>=0:
                        left = mat[row][col-1]

                    mat[row][col] = dungeon[row][col] + max(up,left)

                    if mat[row][col] <=0:
                        mat[row][col] = -float("inf")

            return mat[-1][-1] > 0
        
        l = 1 if dungeon[0][0] >= 0 else abs(dungeon[0][0]) + 1
        h = int(3e5)

        while l <= h:
            mid = (l + h) // 2

            if possible(mid):
                h = mid - 1

            else:
                l = mid + 1 

        return l
            