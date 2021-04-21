import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
	
	def __init__(self):
		self.all_cards=[]
		for suit in suits:
			for rank in ranks:
				self.all_cards.append(Card(suit,rank))

	def shuffle(self):
		return random.shuffle(self.all_cards)

	def deal(self):
		return self.all_cards.pop(0)


class Player(Deck):
	"""docstring for Player"""
	def __init__(self, name):
		self.name=name
		self.hand=[]
		self.ace =0

	def checkforace(self,card):
		if card.rank=='Ace':
			self.ace+=1

	def hit(self):
		self.hand.append(deck.deal())	

	def mycards(self,dealercheck=0):
		if dealercheck==0:
			for x in range(len(self.hand)):
				print(f"{self.hand[x].rank} of {self.hand[x].suit}")
		else:
			print("Card Hidden")
			for x in range(1,len(self.hand)):
				print(f"{self.hand[x].rank} of {self.hand[x].suit}")

	def sum(self):
		sumcards=0
		for x in range(len(self.hand)):
			sumcards+=self.hand[x].value
			if self.hand[x].rank=="Ace" and sumcards>21:
					sumcards-=10
		return sumcards

	def losecheck(self):
		if self.sum()>21:
			return True	
		return False


		
#Game Setup

player =Player(input("Tell us your name : "))
print(f"\n\n\nHello {player.name} \nWelcome to BlackJack \nGet as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.")
dealer =Player("Dealer")
deck =Deck()
deck.shuffle()
player.hit()
dealer.hit()
player.hit()
dealer.hit()


game_on=True 
print("\n\n\nYour cards are : ")
player.mycards()
print("\n\n\nDealer's Cards are :")
dealer.mycards(1)
action=int(input("\n\n\nPress 1 to hit and 0 to stand .\n\n"))
if action==1:
	while game_on:
		if player.losecheck():
			game_on=False
			print("BUST!\nYou Lose!")
			break
		else :
			player.hit()
			print(player.sum())
			player.mycards()
			continue
if action==0:
	while game_on:
		if action==0:
			game_on=False
			print("\n\n\nYour cards are : ")
			player.mycards()
			print("\n\n\nDealer's Cards are :")
			dealer.mycards()
		if dealer.sum()>21:
			print("You Win!")
		elif dealer.sum()>player.sum():
			print("You Lose!")
		elif dealer.sum()==player.sum():
			print("Draw !")
		elif dealer.sum()<=player.sum():
			dealer.hit()
			game_on=True
			continue
		else:
			print("You Win!")
		break