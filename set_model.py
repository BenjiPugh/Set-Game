import random

"""
Model for Set(tm) Game
"""

class SetCard():
    """
    A Representation of a single card from the game of set.
    """
    def __init__(self, qualities):
        """
        Initialize a set card.

        Args:
            qualities: list of ints between 0 and 2 inclusive describing the
            qualities of the card.
        """
        self._qualities = qualities

    def __repr__(self):
        return str(self._qualities)

    @property
    def qualities(self):
        """
        Return the qualities of the set card.
        """
        return self._qualities


class SetDeck():
    """
    A deck of set cards.
    """

    def __init__(self):
        """
        Initialize a full deck of randomized cards.
        """
        self._deck = self.create_deck()
        self.shuffle()

    def create_deck(self):
        """
        Create a full deck of Set cards in which no cards are the same.
        """
        deck = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        deck.append(SetCard([i,j,k,l]))
        return deck

    def shuffle(self):
        """
        Randomize the order of cards
        """
        random.shuffle(self._deck)
    
    def draw(self):
        """
        Take the top Card and remove it from the deck.

        Returns the top SetCard.
        """
        return self._deck.pop(0)

    def __repr__(self):
        representation = ""
        for card in self._deck:
            representation += f"\n {str(card)}"
        return representation
    
    @property
    def deck(self):
        """
        Return the current deck.
        """
        return self._deck

class SetBoard():
    """
    Gameboard Model for set game.
    """
    def __init__(self):
        """
        Initialize deck and deal first 12 cards onto gameboard
        """
        self._deck = SetDeck()
        self._table = []
        self.update_table()
        if brute_force(self._table) == []:
            print("No sets immediately available")

    def update_table(self):
        """
        Top up the cards in table so there are 12 cards on the table.
        """
        
        while len(self._table) < 12 and len(self._deck.deck) > 0:
            self._table.append(self._deck.draw())        

    def __repr__(self):
        return str(self._table)

def check_set(cards):
        """
        Check if any 3 cards are a set.
        """
        set_multiplied = [1, 8, 27, 6]
        for i in range(4):
            multiplied = (cards[0].qualities[i]+1) * (cards[1].qualities[i]+1) * (cards[2].qualities[i]+1)
            if multiplied not in set_multiplied:
                return False
        return True

def brute_force(available_cards):
        """
        Brute force technique for identifying sets.
        """
        sets = []

        for i in range(len(available_cards)-2):
            for j in range(i+1, len(available_cards)-1):
                for k in range(j+1, len(available_cards)):
                    if check_set([available_cards[i], available_cards[j], available_cards[k]]):
                        sets.append((i,j,k))
        return sets