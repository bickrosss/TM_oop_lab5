from dataclasses import dataclass, field

SUITS = '♣ ♦ ♥ ♠'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: list = field(default_factory=make_french_deck)

if __name__ == "__main__":
    deck = Deck()
    print(f"Колода карт создана. Всего карт: {len(deck.cards)}")
    print(f"Первые 5 карт: {deck.cards[:5]}")
    print(f"Последние 5 карт: {deck.cards[-5:]}")