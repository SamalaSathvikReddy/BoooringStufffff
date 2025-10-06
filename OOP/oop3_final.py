import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for i in DeckOfCards.SUITS:
            for j in DeckOfCards.RANKS:
                self.__cards.append((i, j)) 

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if(len(self.__cards) > 0):
            val = self.__cards[0]
            self.__cards.pop(0)
            return val
        return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
