from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

if __name__ == "__main__":
    card = PlayingCard('Q', '♥')
    print(f"Карта: {card}")
    print(f"Масть: {card.suit}, Номинал: {card.rank}")