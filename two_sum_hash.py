def two_sum(arr: list[int], target: int) -> bool:
    complements = {}
    
    for index, num in enumerate(arr):
        complements[target-num]=index
    for index, num in enumerate(arr):
        if num in complements and complements[num]!=index:
            return True
        
        return False