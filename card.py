import random

class Card:
    values = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
    "jack":11, "queen":12, "king":13, "ace":14}
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "jack", "queen", "king", "ace")

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit



# if __name__ == "__main__":
#     two_hearts = Card("two", "hearts")
#     print(two_hearts)
#     print(two_hearts.suit)
#     print(two_hearts.value)