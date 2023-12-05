import random
from typing import List, Dict, Optional, Callable

# Documenting the code - Doesnt change the functionality of Python code. Easier for other developers and auto-complete & linter. 

x: str = 1
y: str = "Valid"
v: List[List[int]] = [[1,2], [3,4]]
xa: Dict[str, str] = {"a": "b"}

def add_this(a: int, b: int) -> int:
    return a + b 

def add_this_b(a: int, b: int) -> int:
    # Still returns - Need a type checker program to look at the code and gives feedback on whether
    # code returns the set type annotations.
    # This is why we use mypy
    return "Hello"

def add_this_c(a: int, b: int) -> int:
    return random.randint(a,b)

print(add_this(2,3))

# 'mypy TypingLD/main.py' -> TypingLD/main.py:7: error: Incompatible return value type (got "str", expected "int")  [return-value]
print(add_this_b(2,3))
print(add_this_c(2,3))



Vector = List[float]
Vectors = List[Vector]

def foo(v: Vector) -> Vector:
    print(v)
    
    
def foo_1(output: Optional[bool]=False):
    pass

def foo_2() -> Callable[[int, int], int]:
    # nested function, "callable(add)", takes two integers and returns an integer 
    def add(x: int, y:int) -> int:
        return x + y 
    
    return add 

def foo_3() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x + y
    
    return func


    




