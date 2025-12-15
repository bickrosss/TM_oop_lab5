from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

if __name__ == "__main__":
    weird_pos = WithoutExplicitTypes(3.14, 'pi day')
    print(f"Динамическая типизация: {weird_pos}")
    print(weird_pos.name, type(weird_pos.name))
    print(weird_pos.value,type(weird_pos.value))