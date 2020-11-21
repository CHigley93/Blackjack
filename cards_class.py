import random
from enum import Enum, auto, IntEnum


class Suit(Enum):
    # card suits, use auto to give unique, incomparable values, since no suit inherently comes before another
    Clubs = auto()
    Diamonds = auto()
    Hearts = auto()
    Spades = auto()

class Rank(IntEnum):

    # Card ranks in order of value
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class Card:

    # Initialize card with valid rank and suit
    def __init__(self, suit, rank: int):

        # Check that the suit is valid
        if not isinstance(suit, Suit):
            raise ValueError("{} is an invalid CardSuit.".format(suit))
        self.suit = suit

        # Check that the rank is valid
        if not isinstance(rank, Rank):
            raise ValueError("{} is an invalid CardRank.".format(rank))
        self.rank = rank
        self.value = [suit, rank]

    # Change the __str__ method so it prints out in "rank of suit" format
    def __str__(self):
        return self.rank.name + " of " + self.suit.name


class Deck:
    # create a standard deck of 52 cards
    def __init__(self):
        self.cards = []
        # self.cards = cards
        for s in Suit:
            for r in Rank:
                self.cards.append(Card(s, r))

    # Change __str__ method so that the deck prints out each card with 13 cards per line
    def __str__(self):
        names = ""
        count = 0
        for card in self.cards:
            names += str(card) + ", "
            count += 1
            if count % 13 == 0:
                names += "\n"
        return names

    # Shuffle method to randomly change the order of the cards
    def shuffle(self):
        random.shuffle(self.cards)

    # deal method to remove cards from the deck and return them as a list
    def deal(self, number: int):
        dealt = []
        if type(number) != int or number < 1:
            raise ValueError("You must choose a positive integer value")
        elif number > len(self.cards):
            raise ValueError("There aren't that many cards to deal")
        else:
            while number > 0:
                dealt.append(self.cards[0])
                del self.cards[0]
                number -= 1
            return dealt

    def pick_by_index(self, i):
        picked = [self.cards[i]]
        del self.cards[i]
        return picked

    def pick_by_value(self, value):
        picked = []
        for card in self.cards:
            if card.value == value:
                picked.append(card)
                return picked
            else:
                raise ValueError("That card is not in this deck")


class Hand(Deck):
    # create an empty list for cards to be put in.
    def __init__(self):
        super().__init__()
        self.cards = []

    def pick_by_value(self, value):
        picked = []
        for card in self.cards:
            if card.value == value:
                picked.append(card)
                return picked
            else:
                raise ValueError("That card is not in this hand")



