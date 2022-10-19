"""
Berilgan son raqamlariga teskari son qaytaring.
Misol uchun:
  reverse_digits(154) => 451
  reverse_digits(710) => 17
"""

def reverse_digits(num: int) -> int:
    result = 0
    while num!=0:
        result*=10
        digit = num%10
        result+=digit
        num//=10
    return result