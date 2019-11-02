import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2): 
        # instance attributes
        self.suit = suit
        self.rank = rank

    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    # def __lt__(self, other):
        # check the suits
        # if self.suit < other.suit: return True
        # if self.suit > other.suit: return False

        # suits are the same... check ranks
        # return self.rank < other.rank

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        # suit를 비교하고 같을 경우 rank를 비교
        return t1 < t2
    # TODO : Write an __lt__ method for Time objects. You can use tuple comparison, but you also might consider comparing integers.

# queen_of_diamonds = Card(1, 12)

card1 = Card(2, 11)
print(card1)
card2 = Card(1, 12)
print(card1 < card2)


class Deck:
    def __init__(self):
        # Deck HAS - A Card
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num) -> None:
        for i in range(num):
            hand.add_card(self.pop_card())

deck = Deck()
print(deck)
deck.shuffle()
print(f'섞인 deck : \n {deck}')
deck.sort()
print(f'소트된 deck : \n {deck}')


# Hand IS - A Deck
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

hand = Hand('new hand')
print(hand.cards)
print(hand.label)


deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)


class Markov:
    
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make on self.suffix_map[self.prefix] = [word]

         self.prefix = shift(self.prefix, word)


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

hand = Hand()
print(find_defining_class(hand, 'shuffle'))

