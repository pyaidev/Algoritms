"""
Ikki arrayda tartiblangan sonlar keltirilgan.
Ularni tartiblangan ko'rinishda birlashtiring.
Misol uchun:
  merge_two_arrays([4,5], [3]) -> [3,4,5]
  merge_two_arrays([1,3], [2,6]) -> [1,2,3,6]
"""

def merge_two_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    i=j=0
    result =[]
    n,m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while i<n:
        result.append(arr1[i])
        i+=1
    while j<m:
        result.append(arr2[j])
        j+=1
    
    return result
        
    