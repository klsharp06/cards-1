import random
import makedeck #rewrite to use this

class Card():
    def __init__(self, Suit, Number, Value):
        self.__Suit = Suit
        self.__Number = Number
        self.__CardValue = Value

    def GetSuit(self):
        return(self.__Suit)
    def GetNumber(self):
        return(self.__Number)

    def GetValue(self):
        return(self.__CardValue)

    def GetCard(self):
        return(str([self.__Number,"of", self.__Suit]).replace('[','').replace(']','').replace("'",'').replace(',',''))

class Deck():
    def __init__(self):
        self.__Deck = []
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for num in range(1, 14):
                match num:
                    case 1:
                        c = Card(suit, "Ace", [1,11])
                    case 11:
                        c = Card(suit, "Jack", 10)
                    case 12:
                        c = Card(suit, "Queen", 10)
                    case 13:
                        c = Card(suit, "King", 10)
                    case _:
                        c = Card(suit, num, num)
                self.__Deck.append(c)
        #^^ the list on card objects

    def ShowDeck(self):
        show = []
        for Card in self.__Deck:
            show.append(Card.GetCard())
        print(show)

    def ShuffleDeck(self):
        random.shuffle(self.__Deck)

    def GetDeck(self):
        return(self.__Deck)

class BlackJack():
    def __init__(self):
        self.PlayerHand = []
        self.DealerHand = []

    def StartGame(self, Deck):
        GameDeck = Deck
        self.PlayerHand = [GameDeck.pop(0), GameDeck.pop(0)]
        self.DealerHand = [GameDeck.pop(0), GameDeck.pop(0)]
        game = True
        turn = 1
        while game:
            print("")
            self.ShowDealerHand(turn)
            self.ShowPlayerHand()

            #player turn
            hand = self.HandValue("player")
            #remove this \/ later?
            if hand[1] == 0:
                print(hand[0], "hand 0")
            else:
                print(hand, "hand")

            valid = False
            while not valid:
                print("Player turn: (stand/hit) ")
                inp = input(">>")
                if inp.upper() == "STAND":
                    #dealer draw till 17 or bust
                    dealDone = False
                    while dealDone == False:
                        value = self.HandValue("dealer")
                        if value[0] < 17 and value[1] < 17:
                            self.DealerHand.append(GameDeck.pop(0))
                            turn+=1
                            self.ShowDealerHand(turn)
                        elif value[0] < 17 and value[1] == 0:
                            self.DealerHand.append(GameDeck.pop(0))
                            turn+=1#
                            self.ShowDealerHand(turn)

                        else:
                            dealDone = True
                            self.ShowDealerHand(turn)
                            
                        if self.Bust("dealer"):
                            print(self.HandValue("dealer"))
                            print("Dealer Bust!")
                            game = False


                    game = False
                    valid = True
                    

                elif inp.upper() == "HIT":
                    self.PlayerHand.append(GameDeck.pop(0))

                    valid = True

            if self.Bust("player"):
                self.ShowPlayerHand()
                # player turn
                print(self.HandValue("player"))
                print("Player Bust!")
                game = False

        #dealer turn
            self.DealerHand.append(GameDeck.pop(0))
            turn += 1
            if self.Bust("dealer"):
                print(self.HandValue("dealer"))
                print("Dealer Bust!")
                game = False

        print("TEST")
        #if second value != 0 and less than 21, ask player to choose which value to use





    def ShowPlayerHand(self):
        cards = []
        for card in self.PlayerHand:
            cards.append(card.GetCard())
        print("Your cards:",", ".join(str(j) for j in cards))

    def ShowDealerHand(self, turn):
        cards = []
        for i in range(0, turn):
            cards.append(self.DealerHand[i].GetCard())
        print("Dealer's Cards:", ", ".join(str(j) for j in cards))


    def Bust(self, P):
        value = self.HandValue(P)
        if value[0] > 21 and value[1] > 21:
            return True
        elif value[0] > 21 and value[1] == 0:
            return True
        else:
            return False


#rewrite for less repeats
    #eg if P = player i = self.PlayerHand,  for c in i:....

    def HandValue(self, P):
        if P == "player":
            value = 0
            if self.HasAce(P):
                aces = 0
                for c in self.PlayerHand:
                    if type(c.GetValue()) is list:
                        aces += 1 ################## <--

                    else:
                        value += c.GetValue()

                value1 = value + aces
                value2 = value + aces + 10

                return value1, value2

            else:
                value = 0
                for c in self.PlayerHand:
                    value += c.GetValue()
                return value, 0
        elif P == "dealer":
            value = 0
            if self.HasAce(P):
                aces = 0
                for c in self.DealerHand:
                    if type(c.GetValue()) is list:
                        aces += 1  ################## <--

                    else:
                        value += c.GetValue()

                value1 = value + aces
                value2 = value + aces + 10

                return value1, value2

            else:
                value = 0
                for c in self.DealerHand:
                    value += c.GetValue()
                return value, 0

    def HasAce(self, P):
        if P == "player":
            for i in self.PlayerHand:
                if i.GetNumber():
                    return True
            return False

        elif P == "dealer":
            for i in self.DealerHand:
                if i.GetNumber():
                    return True
            return False


def CreateGame():
    D = Deck()
    #D.ShowDeck()
    D.ShuffleDeck()
   # D.ShowDeck()

    B = BlackJack()
    B.StartGame(D.GetDeck())


Play = True
while Play:
    CreateGame()
    print("Play again? (Y/N)")
    i = input(">>")
    if i.upper() != "Y":
        Play = False