"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
import cwd
from Card import *
import mycard

class Hist(dict):
    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
    """Represents a poker hand."""
    
    all_labels = ["pair", "twopairs", "threeofakind", "straight", "flush", "fullhouse", "fourofakind", "straightflush"]
                            
    def make_histogram(self):
        """Computes histograms for suits and ranks.

        Creates attributes:

          suits: a histogram of the suits in the hand.
          ranks: a histogram of the ranks.
          sets: a sorted list of the rank sets in the hand.
        """
        self.suits = Hist()
        self.ranks = Hist()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)
            
        self.sets = list(self.ranks.values())   
        self.sets.sort(reverse=True)
        
    def check_sets(self, *t):
        """Checks whether self.sets contains sets that are
        at least as big as the requirements in t.

        t: tuple of ints
        """
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True
             
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Checks if Poker hand has a pair. 
        Returns True if it has a pair or False if otherwise.
        """
        return self.check_sets(2)
        
    def has_twopairs(self):
        """Checks if Poker hand has two pairs. 
        Returns True if it has two pairs or False if otherwise.
        """
        return self.check_sets(2, 2)
        
    def has_threeofakind(self):
        """Checks if Poker hand has three of a kind.
        
        Returns True if it has three of a kind or False if otherwise.
        """
        return self.check_sets(3)
        
    def has_fullhouse(self):
        """Checks if Poker hand has a full house.
        
        Returns True if it has a full house or False if otherwise.
        """
        return self.check_sets(3, 2)

    def has_fourofakind(self):
        """Checks if Poker hand has four of a kind.
        
        Returns True if it has four of a kind or False if otherwise.
        """
        return self.check_sets(4)
        
    def in_a_row(self, ranks, n):
        """Checks whether the histogram has n ranks in a row.

        hist: map from rank to frequency
        n: number we need to get to
        """
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == 5: return True
            else:
                count = 0
        return False
        
    def has_straight(self):
        """Checks whether this hand has a straight."""
        # make a copy of the rank histogram before we mess with it
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        # see if we have 5 in a row
        return self.in_a_row(ranks, 5)

    def has_straightflush(self):
        """Checks whether this hand has a straight flush.

        Better algorithm (in the sense of being more demonstrably
        correct).
        """
        # partition the hand by suit and check each
        # sub-hand for a straight
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)

        # see if any of the partitioned hands has a straight
        for hand in d.values():
            if len(hand.cards) < 5:
                continue            
            hand.make_histogram()
            if hand.has_straight():
                return True
        return False

    def classify(self):
        self.labels = []
        self.make_histogram()
        for label in PokerHand.all_labels:
            f = getattr(self, "has_"+label)
            if f():
                self.labels.append(label)
        

def deal_hands(deck, num_of_hands, num_of_cards):
        """Create appropriate number of Hand objects and deal appropriate number of cards per Hand.
        
        num_of_hands: number of Hand objects to create
        num_of_cards: number of cards per Hand       
        
        returns: list of Hands.
        """
        hands = []
        for i in range(num_of_hands):
            hand = PokerHand()
            deck.move_card(hand, num_of_cards)
            hand.classify()
            hands.append(hand)
        return hands
        
        
def poker_deck(num_of_hands, cards):
    deck = Deck()
    deck.shuffle()
    hands = deal_hands(deck, num_of_hands, cards)  
    
              

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.make_histogram()
        print(hand)
        print(hand.has_flush())
        print(hand.has_pair())
        print(hand.has_twopairs())
        print(hand.has_threeofakind())
        print(hand.has_fullhouse())
        print(hand.has_fourofakind())
        print(hand.has_straight())
        print(hand.has_straightflush())
        print(hand.classify())
        print('')
        

