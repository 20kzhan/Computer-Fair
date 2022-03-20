import random
import time
from UNO.card import *
from UNO.hand import *
from UNO.deck import *

color = ('RED', 'GREEN', 'BLUE', 'YELLOW')
rank = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw2', 'Draw4', 'Wild')
ctype = {'0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number', '6': 'number',
         '7': 'number', '8': 'number', '9': 'number', 'Skip': 'action', 'Reverse': 'action', 'Draw2': 'action',
         'Draw4': 'action_nocolor', 'Wild': 'action_nocolor'}


# Function to check if the card thrown by Player/PC is a valid card by comparing it with the top card
def single_card_check(top_card, card):
    if card.color == top_card.color or top_card.rank == card.rank or card.cardtype == 'action_nocolor':
        return True
    else:
        return False


# FOR PC ONLY
# To check if PC has any valid card to throw
def full_hand_check(hand, top_card):
    for c in hand.cards:
        if c.color == top_card.color or c.rank == top_card.rank or c.cardtype == 'action_nocolor':
            return hand.remove_card(hand.cardsstr.index(str(c)) + 1)
    else:
        return 'no card'


# Function to check if either wins
def win_check(hand):
    if len(hand.cards) == 0:
        return True
    else:
        return False


# Function to check if last card is an action card (GAME MUST END WITH A NUMBER CARD)
def last_card_check(hand):
    for c in hand.cards:
        if c.cardtype != 'number':
            return True
        else:
            return False


def print_rules():
    """Prints the rules at the beginning of the game if told to."""

    print("Setup\n\nAt the start of each round, each player is dealt 7 cards. A card is drawn from the deck"
          "and placed down. This card is the starter card.\n")
    print("Cards\n\nCards come in 2 types, colored and special. Colored cards can be one of 4 colors: "
          "RED, GREEN, BLUE, or YELLOW. Each colored card also has a number on it, from 0-9.")
    print()

def play_game():
    # The gaming loop
    while True:
        # Creating the UNO deck
        game_deck = Deck()
        game_deck.shuffle()

        # Creating the player and PC hands
        player_hand = Hand()
        for i in range(1):
            player_hand.add_card(game_deck.deal())

        pc_hand = Hand()
        for i in range(7):
            pc_hand.add_card(game_deck.deal())

        # Play the first card
        top_card = game_deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = game_deck.deal()
        print(f'\nStarting Card is: {top_card}')
        time.sleep(1)
        playing = True

        # Selecting who goes first
        turn = random.choice(["Player", "Pc"])
        print(turn + ' will go first')

        while playing:
            if turn == 'Player':
                print('\nTop card is: ' + str(top_card))
                print('Your cards: ')
                player_hand.cards_in_hand()
                if player_hand.no_of_cards() == 1:
                    if last_card_check(player_hand):
                        print('Last card cannot be action card \nAdding one card from deck')
                        player_hand.add_card(game_deck.deal())
                        print('Your cards: ')
                        player_hand.cards_in_hand()
                choice = input("\nHit (play a card) or Pull (draw a card)? (h/p): ")
                if choice.lower() in ('h', 'hit'):
                    while True:
                        while True:
                            try:
                                pos = int(input("Enter index of card: "))
                            except TypeError:
                                print("That is not a valid index!")
                            else:
                                break
                        temp_card = player_hand.single_card(pos)
                        if not temp_card:
                            print("That is not a valid index!")
                            continue
                        break
                    if single_card_check(top_card, temp_card):
                        if temp_card.cardtype == 'number':
                            top_card = player_hand.remove_card(pos)
                            turn = 'Pc'
                        else:
                            if temp_card.rank == 'Skip':
                                turn = 'Player'
                                top_card = player_hand.remove_card(pos)
                            elif temp_card.rank == 'Reverse':
                                turn = 'Player'
                                top_card = player_hand.remove_card(pos)
                            elif temp_card.rank == 'Draw2':
                                pc_hand.add_card(game_deck.deal())
                                pc_hand.add_card(game_deck.deal())
                                top_card = player_hand.remove_card(pos)
                                print("PC drew two cards")
                                turn = 'Player'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    pc_hand.add_card(game_deck.deal())
                                top_card = player_hand.remove_card(pos)
                                
                                while True:
                                    draw4color = input('Change color to: ').upper()
                                    
                                    if draw4color not in ("YELLOW", "RED", "BLUE", "GREEN"):
                                        print("I couldn't understand that. Try again?")
                                    else:
                                        break
                                
                                top_card.color = draw4color
                                print(f"Color changed to {draw4color.lower()}.")
                                
                                print("PC drew four cards!")
                                turn = 'Player'
                            elif temp_card.rank == 'Wild':
                                top_card = player_hand.remove_card(pos)
                                wildcolor = input('Change color to: ').upper()
                                top_card.color = wildcolor
                                print(f"Color changed to {wildcolor}")
                                turn = 'Pc'
                    else:
                        print('This card cannot be used')
                elif choice.lower() in ('p', 'pull'):
                    temp_card = game_deck.deal()
                    print('You got: ' + str(temp_card))
                    time.sleep(1)
                    if single_card_check(top_card, temp_card):
                        player_hand.add_card(temp_card)
                    else:
                        print('Cannot use this card')
                        player_hand.add_card(temp_card)
                        turn = 'Pc'
                else:
                    print('I couldn\'t understand that. Try Again?')
                    time.sleep(0.5)

            if turn == 'Pc':
                if pc_hand.no_of_cards() == 1:
                    if last_card_check(pc_hand):
                        time.sleep(1)
                        print('Adding a card to PC hand')
                        pc_hand.add_card(game_deck.deal())
                temp_card = full_hand_check(pc_hand, top_card)
                time.sleep(1)
                if temp_card != 'no card':
                    print(f'\nPC throws: {temp_card}')
                    time.sleep(1)
                    if temp_card.cardtype == 'number':
                        top_card = temp_card
                        turn = 'Player'
                    else:
                        if temp_card.rank == 'Skip':
                            turn = 'Pc'
                            top_card = temp_card
                        elif temp_card.rank == 'Reverse':
                            turn = 'Pc'
                            top_card = temp_card
                        elif temp_card.rank == 'Draw2':
                            player_hand.add_card(game_deck.deal())
                            player_hand.add_card(game_deck.deal())
                            top_card = temp_card
                            turn = 'Pc'
                        elif temp_card.rank == 'Draw4':
                            for i in range(4):
                                player_hand.add_card(game_deck.deal())
                            top_card = temp_card
                            draw4color = pc_hand.cards[0].color
                            print('Color changes to', draw4color)
                            top_card.color = draw4color
                            turn = 'Pc'
                        elif temp_card.rank == 'Wild':
                            top_card = temp_card
                            wildcolor = pc_hand.cards[0].color
                            print("Color changes to", wildcolor)
                            top_card.color = wildcolor
                            turn = 'Player'
                else:
                    print('\nPC pulls a card from deck')
                    time.sleep(1)
                    temp_card = game_deck.deal()
                    if single_card_check(top_card, temp_card):
                        print(f'PC throws: {temp_card}')
                        time.sleep(1)
                        if temp_card.cardtype == 'number':
                            top_card = temp_card
                            turn = 'Player'
                        else:
                            if temp_card.rank == 'Skip':
                                turn = 'Pc'
                                top_card = temp_card
                            elif temp_card.rank == 'Reverse':
                                turn = 'Pc'
                                top_card = temp_card
                            elif temp_card.rank == 'Draw2':
                                player_hand.add_card(game_deck.deal())
                                player_hand.add_card(game_deck.deal())
                                top_card = temp_card
                                turn = 'Pc'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    player_hand.add_card(game_deck.deal())
                                top_card = temp_card
                                draw4color = pc_hand.cards[0].color
                                print('Color changes to', draw4color)
                                top_card.color = draw4color
                                turn = 'Pc'
                            elif temp_card.rank == 'Wild':
                                top_card = temp_card
                                wildcolor = pc_hand.cards[0].color
                                print('Color changes to', wildcolor)
                                top_card.color = wildcolor
                                turn = 'Player'
                    else:
                        print('PC doesnt have a card')
                        time.sleep(1)
                        pc_hand.add_card(temp_card)
                        turn = 'Player'
                print(f'\nPC has {pc_hand.no_of_cards()} cards remaining')
                time.sleep(1)
            if win_check(pc_hand):
                print('\nYou lost..')
                playing = False
            elif win_check(player_hand):
                print('\nYou Won!!')
                playing = False

        # Start a new round or end game
        new_game = input('Would you like to play UNO again? (y/n)')
        if new_game == 'y':
            continue
        else:
            print('\nThanks for playing!!')
            break