"""
1dan N gacha bo'lgan toq sonlar yig'indisini O(1) da hisoblang.
Misol uchun:
  sum_of_odd_numbers(5) = 9, chunki 1+3+5 = 9
  sum_of_odd_numbers(8) = 16, chunki 1+3+5+7 = 16
"""

def sum_of_odd_numbers(n: int) -> int:
    summa =0
    for num in range(1, n+1, 2):
        summa = summa + num
    return summa
            