"""
Berilgan son ikkining darajasi ekanligiga tekshiring.
Misol uchun:
  is_power_of_two(16) => True
  is_power_of_two(15) => False
"""

def is_power_of_two(num: int) -> bool:
    bit_count = 0
    while num!=0:
        bit_count += num & 1
        num = num >> 1
        
    return bit_count ==1