"""
Tartiblangan sonlar ro'yhati va qidirilayotgan son berilgan.
Array ichida berilgan son borligiga tekshiring.
Misol uchun:
  binary_search_recursive([1,4,5,7], 3) => False
  binary_search_recursive([1,4,5,7], 5) => True
"""

# slice
# def binary_search_recursive(arr: list[int], target: int) -> bool:
#     """
#     Kodni bu yerda yozing.
#     """
#     if not arr:
#         return False
#
#     mid = len(arr) // 2
#     if arr[mid] == target:
#         return True
#
#     if arr[mid] < target:
#         return binary_search_recursive(arr[mid + 1:], target)
#     return binary_search_recursive(arr[:mid], target)
#
#
# print(binary_search_recursive(arr=[1,2,3,4,5,6], target=10))

def bs(arr, target, left, right):
    if left>right:
        return False
    mid = (left+right) // 2
    if arr[mid] == target:
        return True

    if arr[mid] < target:
        return bs(arr, target, mid+1, right)
    return bs(arr, target, left, mid-1)
def binary_search_recursive(arr: list[int], target: int) -> bool:
    return bs(arr, target, 0, len(arr)-1)
