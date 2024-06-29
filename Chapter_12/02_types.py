from typing import List, Tuple, Dict, Union

n: int = 5


name: str = "string"
name: str = 3

print(type(name), name)  # <class 'int'> 3


def sum(a: int, b: int) -> int:
    return a + b


print(sum(1, 3))


numbers: List[int] = [1, 2, 3, 4, 5, 6]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

identifier: Union[int, str] = "ID123"
identifier = 12345
