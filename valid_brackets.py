"""
Berilgan qavslar to'g'ri yopilganligiga tekshiring.
Qavslar - (), {}, [].
Misol uchun:
  valid_brackets("()()") = True
  valid_brackets("{()[]}") = True
  valid_brackets("{(]}") = False
"""

def valid_brackets(s: str) -> bool:
    stack = []
    bracket = {
        
        "}":"{",
        "]":"[",
        ")":"(",
    }
    
    for char in s:
        if char not in bracket:
            stack.append(char)
            continue
        
        if not stack:
            return False
        
        if not stack or stack.pop() != bracket[char]:
            return False
    return not stack