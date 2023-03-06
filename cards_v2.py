import random, itertools, shelve, pickle


class CardDeck():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    small_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    shuffle_deck = False
    deck = []

    def shuffle(self):
        random.shuffle(self.deck)
        shuffle_deck = True
        return self.deck

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, key):
        item = self.deck[key]
        if not isinstance(key, slice):
            return (item,)
        return tuple(item)

    def __add__(self, new_card):
        if isinstance(new_card, list):
            for card in new_card:
                self.deck.append(card)
        else:
            self.deck.append(new_card)
        return self.deck

    def __contains__(self, card):
        return (card in self.deck)

    def __eq__(self, other):
        if self.deck == other:
            return True
        return False

    def __sub__(self, cards_delete):
        if isinstance(cards_delete, list):
            for card in cards_delete:
                self.deck.remove(card)
        else:
            self.deck.remove(cards_delete)
        return self.deck

    def save(self, deck_name):
        f = shelve.open('filename')
        f[deck_name] = self.deck
        f.close()

    def load(self, deck_name):
        file = shelve.open('filename')
        print(file[deck_name])

class SmallDeck(CardDeck):

    def __init__(self):
        self.deck = []
        self.deck_cr()

    def __str__(self):
        return f'Deck is {self.deck}'

    def deck_cr(self):
        self.deck = list(itertools.product(CardDeck.small_ranks, CardDeck.suits))
        return self.deck

class ClassicDeck(CardDeck):

    def __init__(self):
        self.deck = []
        self.deck_cr()

    def __str__(self):
        return f'Deck is {self.deck}'

    def deck_cr(self):
        self.deck = list(itertools.product(CardDeck.ranks, CardDeck.suits))
        return self.deck

if __name__ == '__main__':
    a = ClassicDeck()
    b = SmallDeck()
    # a.save("Classic deck")
    # b.save("Small deck")
    # a.load("Classic deck")
    # b.load("Small deck")