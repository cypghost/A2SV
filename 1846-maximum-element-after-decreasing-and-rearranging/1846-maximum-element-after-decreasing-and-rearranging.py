class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        subs = [0] * (len(arr) - 1)

        for index in range(len(arr) - 1):
            subs[index] = abs(arr[index] - arr[index - 1])
        
        if set(subs) not in [0, 1]:
            for index in range(1, len(arr)):
                if abs(arr[index] - arr[index - 1]) > 1:
                    arr[index] = arr[index - 1] + 1

        return max(arr)