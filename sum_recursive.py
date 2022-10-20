"""
Berilgan sonlar yig'indisini rekursiya orqali hisoblang.
Misol uchun:
  sum_recursive([1,3]) => 4
  sum_recursive([4,5,2]) => 11
"""

def sum_recursive(nums: list[int], index=0) -> int:
    if index == len(nums):
        return 0
        
    return nums[index]+sum_recursive(nums, index+1)