# user and computer should get two random cards
#cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
import random

user_cards = []  # list for user cards
computer_cards = []  # list for computer cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # card list to chose from
card = random.choice(cards)# randomly choice a card by computer
#adding these cards to the user and computer list
user_cards.append(card)

#  print(card) # print that random card


