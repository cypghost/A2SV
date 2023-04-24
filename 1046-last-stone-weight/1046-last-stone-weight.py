class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while stones:
            s1 = stones.pop()

            if not stones: 
                return s1

            s2 = stones.pop()

            if s1 > s2:
                insort_left(stones, s1 - s2)
 
        return 0 