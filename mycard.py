class Card:
    """Represents a standard playing card.
    
    Attributes: 
        suit: integer 0-3
        rank: integer 1-13
    """
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    # class attributes
    suit_names = ["Club", "Diamond", "Hearts", "Spade"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
    def __str__(self):
        return "{0} of {1}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])
        
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
        
        
class Deck:
    """Represents a deck of playing cards."""
    
    def __init__(self):
        self.cards = []
        # build the list of cards
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)      

    def add_card(self, card):
        self.cards.append(card)   
        
    def deal_hands(self, num_of_hands, num_of_cards):
        """Create appropriate number of Hand objects and deal appropriate number of cards per Hand.
        
        num_of_hands: number of Hand objects to create
        num_of_cards: number of cards per Hand       
        
        returns: list of Hands.
        """
        res = []
        self.shuffle()
        for i in range(num_of_hands):
            hand = Hand("hand {}".format(i))
            self.move_card(hand, num_of_cards)
            res.append(hand)
        return res
        
        
    def move_card(self, hand, num):
        """Move given number of cards between deck and hand and vice-versa."""
        for i in range(num):
            hand.add_card(self.pop_card())
        
    def pop_card(self):
        return self.cards.pop() 
        
    def shuffle(self):
        import random
        random.shuffle(self.cards)    
        
    def sort(self):
        """Sort cards in ascending order."""
        self.cards.sort()
        
        
#inherits from Deck        
class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=""):
        self.cards = []
        self.label = label
            
       
if __name__ == "__main__":
    #card1 = Card(2, 10)
    #card2 = Card(2, 12)
    #print(card1)
    #print(card2)
    #print(card1 > card2)
    deck = Deck()
    hands = deck.deal_hands(5, 4)
    for hand in hands:
        print(hand)
    
        
    