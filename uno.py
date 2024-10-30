import random
#Viva mexico 
def start_game():
    # Set up Uno deck
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))
    special_cards = ("+2", "Block turn")
    
    deck = [(colour, rank) for colour in colours for rank in ranks] + [(colour, special_card) for colour in colours for special_card in special_cards]

    # Shuffle the deck
    random.shuffle(deck)

    # Each player gets 7 cards
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    # Central card
    central_card = deck.pop(0)

    # We start with player 1's turn (0 = player 1, 1 = player 2)
    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):
    while len(p1) > 0 and len(p2) > 0:
        if whose_turn == 0:
            # Player 1's turn
            print(f"\nPlayer 1's turn, here is your hand: {p1}")
            print(f"Central card is: {central_card}")

            # Give the user a choice, play a card or draw a card
            ans = int(input("You have a choice, (0) draw or (1) play: "))

            # Handle playing a card
            if ans == 1:
                player_choice = int(input("Which card to play (1-based index)? ")) - 1
                if 0 <= player_choice < len(p1):
                    valid = valid_play(central_card, p1[player_choice])
                    if valid:
                        card_to_play = p1.pop(player_choice)
                        central_card = card_to_play
                        print(f"Player 1 played: {card_to_play}")

                        # Handle special cards
                        if card_to_play[1] == "+2":
                            # Player 2 draws 2 cards
                            print("Player 2 must draw 2 cards!")
                            for _ in range(2):
                                if len(deck) > 0:
                                    p2.append(deck.pop(0))
                                else:
                                    print("The deck is empty, no more cards to draw.")
                        elif card_to_play[1] == "Block turn":
                            print("Player 2's turn is blocked!")
                            continue  # Skip Player 2's turn

                        if len(p1) == 0:
                            print("Player 1 wins!")
                            exit()
                    else:
                        print("Invalid card choice.")
                else:
                    print("Invalid card index.")
            elif ans == 0:
                # Handle drawing a card
                if len(deck) > 0:
                    drawn_card = deck.pop(0)
                    p1.append(drawn_card)
                    print(f"Player 1 drew: {drawn_card}")
                else:
                    print("The deck is empty, no more cards to draw.")

        else:
            # AI (Player 2) turn logic could go here
            print("AI's turn (not yet implemented)")
            # You can add AI logic for Player 2 here

        # Change turns
        whose_turn = (whose_turn + 1) % 2

    # End of game conditions
    if len(p1) == 0:
        print("Player 1 wins!")
    elif len(p2) == 0:
        print("Player 2 wins!")

# Validate if two cards can be played on top of each other
def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()

