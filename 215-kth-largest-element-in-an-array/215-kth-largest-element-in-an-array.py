# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) <= 1:
#             return nums[0]

#         def quicksort(arr, low, high):
#             if low < high:
#                 pi = partition(arr, low, high)
#                 quicksort(arr, low, pi - 1)
#                 quicksort(arr, pi + 1, high)

#             return arr

#         def partition(arr, low, high):
#             pivot = arr[high]

#             left = low - 1

#             for index in range(low, high):
#                 if arr[index] <= pivot:
#                     left += 1
#                     arr[index], arr[left] = arr[left], arr[index]
                    

#             arr[left + 1], arr[high] = arr[high], arr[left + 1]

#             return left + 1

#         return quicksort(nums, 0, len(nums) - 1)[len(nums) - k]

    
    
class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
            
        pivot = random.choice(nums)
            
        
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        
        else:
            return mid[0]
