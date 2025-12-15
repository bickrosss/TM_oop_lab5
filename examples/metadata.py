from dataclasses import dataclass, field

@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

if __name__ == "__main__":
    pos = Position('Equator', 0.0, 0.0)
    print(f"Позиция: {pos}")
    
    from dataclasses import fields
    for f in fields(pos):
        print(f"Поле {f.name}: metadata = {f.metadata}")