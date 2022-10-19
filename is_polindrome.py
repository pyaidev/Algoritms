"""
Berilgan so'z palindrom ekanligiga tekshiring.
Misol uchun:
  is_palindrome("kiyik") = True
  is_palindrome("aziza") = True
  is_palindrome("anora") = False
"""

def is_palindrome(word: str) -> bool:
    
    low, high = 0, len(word)-1
    while low<high:
        if word[low]!=word[high]:
           return False
        low+=1
        high-=1
    return True