class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd = ""

        for i in range(len(num)):
            current_digit = int(num[i])

            if current_digit % 2 == 1:
                current_odd = num[:i+1]
                max_odd = max(max_odd, current_odd)

        return max_odd

