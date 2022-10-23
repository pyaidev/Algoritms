"""
Tartiblangan sonlar ro'yhati va qidirilayotgan son berilgan.
Array ichida berilgan son borligiga tekshiring.
Misol uchun:
  binary_search_iterative([1,4,5,2], 3) => False
  binary_search_iterative([1,4,5,2], 5) => True
"""


def binary_search_iterative(arr: list[int], target: int) -> bool:
    """
    Kodni bu yerda yozing.
    """
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return False

