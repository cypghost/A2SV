class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum_of_minimums = 0;

        for index in range(len(arr) + 1):
            while stack and (index == len(arr) or arr[stack[-1]] >= arr[index]):

                mid = stack.pop()
                
                if not stack :
                    left = -1 
                    
                else:
                    left = stack[-1]
                    
                right = index

                
                count = (mid - left) * (right - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(index)
        
        return sum_of_minimums % (10 ** 9 + 7)