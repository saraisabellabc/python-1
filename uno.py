#Feodor and Isabella fused code
#Uno version that has +2, Black Cards and Skip Turn
#Assume there is only 2 players and that players won't cheat and look at other players' cards
#You can add special cards later,
import random

def start_game():
    colors = ('Blue', 'Green', 'Red', 'Yellow')
    ranks = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', "+2", "Block Turn")
    #Special Black Cards
    S_ranks = ("+4", "Change Color")
    S_colors = ('Black','Black' )

    deck = [(rank, color) for rank in ranks for color in colors]
    special_deck = [(power, color) for power in S_ranks for color in S_colors for _ in range(2)]
    deck = deck + special_deck
    random.shuffle(deck)

    p1 = [deck.pop() for _ in range(7)]
    p2 = [deck.pop() for _ in range(7)]

    center_card = deck.pop()
    while center_card[1] == "Black":
        deck.append(center_card)
        center_card = deck.pop()
    turn = random.randint(1, 2)
    play_turn(p1, p2, deck, center_card, turn)

def play_turn(p1, p2, deck, center_card, turn):
    #Assign the turns cards
    #REREAD LATER, does Python attribute 'cards' as a pointer to p1 or p2?
    while True:
        if turn == 1:
            cards = p1
            opposite = p2

            print(f"\n*The center card is: {center_card}")
            print(f"  Player {turn}, your cards are: {cards}")

            #Playable cards
            available_cards = playable_cards(cards, center_card)
            print(f"  Your playable cards are: {available_cards}")

            #Check if no cards are playable
            if len(available_cards) == 0:
                print("  No cards can be played, you must DRAW")
                cards.append(deck.pop())
            else:
                choice = int(input("  Do you want to PLAY A CARD(0) or DRAW A CARD(1)? "))
                if choice == 1:
                    if len(deck) == 0:
                        #Recheck later, might not be necessary or there might be a better way to do this
                        print("  Since the deck is empty, it will be reshuffled")
                        #reshuffle_deck(deck, center_card)
                    cards.append(deck.pop())
                elif choice == 0:
                    card_choice = int(input(f"  Pick which card to play through its place in the order, starting from 1: "))
                    if 1 <= card_choice <= len(available_cards):
                        deck.append(center_card)
                        center_card = cards.pop(cards.index(available_cards[card_choice - 1]))
                        if len(cards) == 0:
                            print(f"\n  Player {turn} wins!")
                            return
                        if len(cards) == 1:
                            print("\nUNO!\n")

                        #SPECIAL CARDS:
                        #Code to for "+2"
                        if center_card[0] == "+2":
                            opposite.extend(deck.pop() for _ in range(2))

                        #Code to for "+4"
                        elif center_card[0] == "+4":
                            opposite.extend(deck.pop() for _ in range(4))
                            requested_color = input("  What color do you want to change to: Red, Green, Blue, or Yellow? ").capitalize()
                            while requested_color not in ['Red', 'Green', 'Blue', 'Yellow']:
                                requested_color = input("  Only choose from Red, Green, Blue, or Yellow: ").capitalize()
                            center_card = ("+4", requested_color)
                            print(f"  The new color is {requested_color}")

                        #Code for "Block Turn
                        elif center_card[0] == "Block Turn":
                            continue

                        #Code for Change Color
                        elif center_card[0] == "Change Color":
                            requested_color = input("  What color do you want to change to: Red, Green, Blue, or Yellow? ").capitalize()
                            while requested_color not in ['Red', 'Green', 'Blue', 'Yellow']:
                                requested_color = input("  Only choose from Red, Green, Blue, or Yellow: ").capitalize()
                            center_card = ("Change Color", requested_color)
                            print(f"  The new color is {requested_color}")
        else:
            cards = p2
            opposite = p1

            #Playable cards
            available_cards = playable_cards(cards, center_card)

            #Check if no cards are playable
            if len(available_cards) == 0:
                print("\n*No cards can be played, the AI must DRAW")
                cards.append(deck.pop())
            else:
                deck.append(center_card)
                print(f"\n*The AI played {available_cards[0]}")
                center_card = cards.pop(cards.index(available_cards[0]))
                if len(cards) == 0:
                    print(f"\n  The AI wins!")
                    return
                if len(cards) == 1:
                    print("\nUNO for AI!")
                #SPECIAL CARDS:
                #Code to for "+2"
                if center_card[0] == "+2":
                    opposite.extend(deck.pop() for _ in range(2))
                #Code to for "+4"
                elif center_card[0] == "+4":
                    opposite.extend(deck.pop() for _ in range(4))
                    requested_color = random.choice(["Red", "Green", "Blue", "Yellow"])
                    center_card = ("+4", requested_color)
                    print(f"  The new color is {requested_color}")
                #Code for "Block Turn
                elif center_card[0] == "Block Turn":
                    continue
                #Code for Change Color
                elif center_card[0] == "Change Color":
                    requested_color = random.choice(["Red", "Green", "Blue", "Yellow"])
                    center_card = ("Change Color", requested_color)
                    print(f"  The new color is {requested_color}")
            
        #Change turns
        turn = 1 if turn == 2 else 2

#Returns a list of all playable cards
def playable_cards(cards, center_card):
    return [card for card in cards if card[0] == center_card[0] or card[1] == center_card[1] or card[1] == "Black"]

#RESHUFFLE
#Commented out because not yet sure if it works well
#def reshuffle_deck(deck, center_card):
    #deck.append(center_card)
    #random.shuffle(deck)

#START THE GAME HERE
start_game()

