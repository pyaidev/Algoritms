"""
Rekursiya orqali, berilgan so'zga teskari so'z qaytaring.
Misol uchun:
  reverse_recursive("space") => "ecaps"
  reverse_recursive("where") => "erehw"
"""

def reverse_recursive(word: str) -> str:
    if word == "":
        return word
        
    reversed_str = reverse_recursive(word[1:])
    return reversed_str + word[0]