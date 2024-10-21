import random

class Card():
    def __init__(self, Suit, Number):
        self.__Suit = Suit
        self.__Number = Number

    def GetSuit(self):
        return(self.__Suit)
    def GetNumber(self):
        return(self.__Number)

    def GetCard(self):
        return([self.__Number, self.__Suit])


class Deck():
    def __init__(self):
        self.__Deck = []
        for suit in ["Heart", "Spade", "Diamond", "Club"]:
            for num in range(1, 14):
                match num:
                    case 1:
                        c = Card(suit, "Ace")
                    case 11:
                        c = Card(suit, "Jack")
                    case 12:
                        c = Card(suit, "Queen")
                    case 13:
                        c = Card(suit, "King")
                    case _:
                        c = Card(suit, num)
                self.__Deck.append(c)
        #^^ the list on card objects

    def ShowDeck(self):
        show = []
        for Card in self.__Deck:
            show.append(Card.GetCard())
        print(show)

    def ShuffleDeck(self):
        random.shuffle(self.__Deck)



def CreateDeck():
    D = Deck()
    D.ShowDeck()
    D.ShuffleDeck()
    D.ShowDeck()