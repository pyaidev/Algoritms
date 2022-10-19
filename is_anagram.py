"""
Berilgan ikki so'z anagram ekanligiga tekshiring.
Misol uchun:
  is_anagram("lama", "alam") => True
  is_anagram("mosh", "shom") => True
  is_anagram("non", "nok") => False
"""

def build_counter(word):
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char]=1
            continue
        counter[char]+=1
    return counter

def is_anagram(word1: str, word2: str) -> bool:
    counter1 = build_counter(word1)
    counter2 = build_counter(word2)
    
    return counter1==counter2