import time
import random

time.sleep(1)

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]
# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
p1 = [deck.pop() for _ in range(26)]
p2 = [deck.pop() for _ in range(26)]

def card_comparison(p1_card, p2_card):
    """Compares two cards to determine the stronger one.
       Returns 1 if Player 1's card is stronger, 2 if Player 2's card is stronger,
       and 0 if the cards are equal.
    """
    return 1 if ranks.index(p1_card[0]) > ranks.index(p2_card[0]) else 2 if ranks.index(p1_card[0]) < ranks.index(p2_card[0]) else 0

def play_round(player1_hand, player2_hand):
    """Plays a single round of the game.
       Each player flips a card, and the winner is determined using the card_comparison function.
       If both players flip the same value card, call the war function.
    """
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    print(f"Player 1's Card: {card1}, Player 2's Card: {card2}")

    # Use `comparison_result` to store the outcome of the comparison
    comparison_result = card_comparison(card1, card2)

    if comparison_result == 0:
        print("\nPeace!\n")
        war(player1_hand, player2_hand, [card1, card2])
    elif comparison_result == 1:
        print("Player 1 has won the round")
        player1_hand.extend([card1, card2])
        random.shuffle(player1_hand)  # Shuffle to avoid infinite loops
    else:
        print("Player 2 has won the round")
        player2_hand.extend([card1, card2])
        random.shuffle(player2_hand)

def war(player1_hand, player2_hand, pile):
    """Handles the 'war' scenario when cards are equal.
       Both players put 3 cards face down, then both players flip a 4th card.
       The player with the stronger card takes all the cards.
    """
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        # Handle cases where a player doesn't have enough cards for war
        if len(player1_hand) == 0 and len(player2_hand) == 0:
            print("It's a tie, no winner.")
            exit()
        elif len(player1_hand) == 0:
            print("Player 2 has won the game!")
            exit()
        elif len(player2_hand) == 0:
            print("Player 1 has won the game!")
            exit()

        # Add remaining cards to the pile if a player runs out during war
        pile.extend([player1_hand.pop(0) for _ in range(len(player1_hand))] + [player2_hand.pop(0) for _ in range(len(player2_hand))])
        print("A player ran out of cards during war.")
        return

    # Add the face-down cards to the pile
    pile.extend([player1_hand.pop(0) for _ in range(3)] + [player2_hand.pop(0) for _ in range(3)])
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    print(f"Player 1's Card: {card1}, Player 2's Card: {card2}")

    # Use `comparison_result` to store the outcome of the comparison
    comparison_result = card_comparison(card1, card2)

    if comparison_result == 0:
        print("\nPeace!\n")
        war(player1_hand, player2_hand, [card1, card2])
    elif comparison_result == 1:
        print("Player 1 has won the round")
        player1_hand.extend([card1, card2])
        random.shuffle(player1_hand)  # Shuffle to avoid infinite loops
    else:
        print("Player 2 has won the round")
        player2_hand.extend([card1, card2])
        random.shuffle(player2_hand)

def war(player1_hand, player2_hand, pile):
    """Handles the 'war' scenario when cards are equal.
       Both players put 3 cards face down, then both players flip a 4th card.
       The player with the stronger card takes all the cards.
    """
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        # Handle cases where a player doesn't have enough cards for war
        if len(player1_hand) == 0 and len(player2_hand) == 0:
            print("It's a tie, no winner.")
            exit()
        elif len(player1_hand) == 0:
            print("Player 2 has won the game!")
            exit()
        elif len(player2_hand) == 0:
            print("Player 1 has won the game!")
            exit()

        # Add remaining cards to the pile if a player runs out during war
        pile.extend([player1_hand.pop(0) for _ in range(len(player1_hand))] + [player2_hand.pop(0) for _ in range(len(player2_hand))])
        print("A player ran out of cards during war.")
        return

    # Add the face-down cards to the pile
    pile.extend([player1_hand.pop(0) for _ in range(3)] + [player2_hand.pop(0) for _ in range(3)])
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    print(f"Player 1's War Card: {card1}, Player 2's War Card: {card2}")

    # Use `comparison_result` in the war scenario
    comparison_result = card_comparison(card1, card2)

    if comparison_result == 0:
        print("\nAnother tie during war!\n")
        war(player1_hand, player2_hand, pile + [card1, card2])
    elif comparison_result == 1:
        print("Player 1 wins the war round")
        player1_hand.extend(pile + [card1, card2])
    else:
        print("Player 2 wins the war round")
        player2_hand.extend(pile + [card1, card2])

def play_game():
    """Main function to run the game."""
    while len(p1) > 0 and len(p2) > 0:
        print(f"P1 has {len(p1)} cards left, P2 has {len(p2)} cards left\n")
        play_round(p1, p2)

        # Check if any player has won
        if len(p1) == 0:
            print("Player 2 has won the game!")
            exit()
        elif len(p2) == 0:
            print("Player 1 has won the game!")
            exit()

# Start the game
play_game()

