import random


class Card:
    # possible values for rank and suit
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = [1, 2, 3, 4]

    # Initialize card with valid rank and suit
    def __init__(self, suit: int, rank: int):
        if suit not in self.suits:
            raise ValueError("%d is not a valid suit." % suit)
        if rank not in self.nums:
            raise ValueError("%d is not a valid title." % rank)

        self.suit = suit
        self.rank = rank
        self.value = [suit, rank]

    # Change the __str__ method so it prints out in "rank of suit" format
    def __str__(self):
        if self.suit == 1:
            suit = "Clubs"
        elif self.suit == 2:
            suit = "Diamonds"
        elif self.suit == 3:
            suit = "Hearts"
        elif self.suit == 4:
            suit = "Spades"

        if self.rank == 1:
            rank = "Ace"
        elif 1 < self.rank < 11:
            rank = str(self.rank)
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"

        return rank + " of " + suit


class Deck:
    # create a standard deck of 52 cards
    def __init__(self):
        self.cards = []
        # self.cards = cards
        for s in range(1, 5):
            for r in range(1, 14):
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
        if type(number) != int or number < 1:
            raise ValueError("You must choose a positive integer value")
        dealt = []
        while number > 0:
            dealt.append(self.cards[0])
            del self.cards[0]
            number -= 1
        return dealt


class Hand:
    # create an empty list for cards to be put in.
    def __init__(self):
        self.cards = []

    # String method for showing the cards in the hand
    def __str__(self):
        names = ""
        count = 0
        for card in self.cards:
            names += str(card) + ", "
            count += 1
            if count % 13 == 0:
                names += "\n"
        return names

    # deal method to remove cards from the deck and return them as a list
    def deal(self, number: int):
        if type(number) != int or number < 1:
            raise ValueError("You must choose a positive integer value")
        dealt = []
        while number > 0:
            dealt.append(self.cards[0])
            del self.cards[0]
            number -= 1
        return dealt