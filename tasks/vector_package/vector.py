from dataclasses import dataclass
from typing import Generic, TypeVar
import math

T = TypeVar("T", int, float)


@dataclass(eq=False)
class Vector(Generic[T]):
    x: T
    y: T
    
    def __post_init__(self) -> None:
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise TypeError("Координаты должны быть числами")
    
    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        
        return abs(self.length() - other.length()) < 1e-10
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y}, length={self.length():.2f})"