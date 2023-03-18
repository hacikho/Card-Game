from card import Card
import random
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in Card.suits:
            for rank in Card.ranks:
                #Create a card object
                created_card = Card(rank, suit)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

if __name__ == "__main__":
    new_deck = Deck()
    new_deck.shuffle()
    mycard = new_deck.deal_one()
    print(mycard)
    print(len(new_deck.all_cards))

    # for card_object in new_deck.all_cards:
    #     print(card_object)