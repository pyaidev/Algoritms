"""
Berilgan sonni ikkilik sanoqga o'tkazing.
Misol uchun:
    convert_to_binary(6) => "110"
    convert_to_binary(13) => "1101"
"""

def convert_to_binary(num: int) -> str:
    result= ""
    while num!=0:
        digit = num%2
        result +=str(digit)
        num//=2
    return result[::-1]
            