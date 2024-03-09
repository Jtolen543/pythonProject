import p1_random as p1
rng = p1.P1Random()

def game_menu():
    # prints out the game menu
    print("1.  Get another card")
    print("2.  Hold hand")
    print("3.  Print statistics")
    print("4.  Exit\n")

def card_names(card_value):
    # made a function that renames the card value if it deals a face card or ace
    match card_value:
        case 1:
            return "ACE"
        case 11:
            return "JACK"
        case 12:
            return "QUEEN"
        case 13:
            return "KING"
        case other:
            return card_value

game_number = 1
progress_start = True
print_card = True
dealer_wins = 0
player_wins = 0
game_ties = 0

while progress_start: # continues the progress as long as user does not exit program
    print(f"START GAME #{game_number}")
    game_start = True # moved this block of variables inside the while loop to act as a reset for the a finished game
    card_value = rng.next_int(13) + 1
    hand_value = 0
    if card_value == 11 or card_value == 12 or card_value == 13:
        hand_value += 10
    else:
        hand_value += card_value
    while game_start:
        card_names(card_value)
        # placed the function here since it is a primarily relates to game output
        match print_card:
            case True:
                print(f"\nYour card is a {card_names(card_value)}!")
                print(f"Your hand is: {hand_value}\n")
            case other:
                print_card = True
        game_menu()
        # same case with card_names()
        option_choice = int(input("Choose an option: "))
        if option_choice == 1:
            # will generate a random integer every time a card is dealt
            card_value = rng.next_int(13) + 1
            if card_value == 11 or card_value == 12 or card_value == 13:
                hand_value +=10 # added a condition that makes it where 10 is added to hand for face cards
            else:
                hand_value += card_value # updates the hand value value
            if hand_value == 21:
                print(f"\nYour card is a {card_names(card_value)}!")
                print(f"Your hand is: {hand_value}")
                print("\nBLACKJACK! You win!\n")
                player_wins += 1
                game_number += 1
                break
            elif hand_value > 21:
                print(f"\nYour card is a {card_names(card_value)}!")
                print(f"Your hand is: {hand_value}\n")
                print("You exceeded 21! You lose.\n")
                dealer_wins += 1
                game_number += 1
                break
            else:
                True
        elif option_choice == 2:
            # will generate a number between 16 and 26 and see if the player wins, loses or ties
            dealer_hand = rng.next_int(11) + 16
            if dealer_hand > 21:
                # the games automatically says you win if the dealer hand is over 21 and restarts
                print(f"\nDealer's hand: {dealer_hand}")
                print(f"Your hand is: {hand_value}\n")
                print("You win!\n")
                player_wins += 1
                game_number += 1
                break
            elif dealer_hand == hand_value:
                # the game automatically draws if you and the dealer have the same value
                print(f"\nDealer's hand: {dealer_hand}")
                print(f"Your hand is: {hand_value}\n")
                print("It's a tie! No one wins!\n")
                game_ties += 1
                game_number += 1
                break
            elif dealer_hand > hand_value:
                # dealer wins if you have a lesser value
                print(f"\nDealer's hand: {dealer_hand}")
                print(f"Your hand is: {hand_value}\n")
                print("Dealer wins!\n")
                dealer_wins += 1
                game_number += 1
                break
            else:
                print(f"\nDealer's hand: {dealer_hand}")
                print(f"Your hand is: {hand_value}\n")
                print("You win!\n")
                player_wins += 1
                game_number += 1
                # this else statement covers if you have a greater value than the dealer
                break
        elif option_choice == 3:
            print(f"\nNumber of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_number - 1}")
            if game_number >= 2:
                print(f"Percentage of Player wins: {round(100*player_wins / (game_number - 1),1)}%\n")
            else:
                print(f"Percentage of Player wins: {round(100 * player_wins / (game_number), 1)}%\n")
            print_card = False
        elif option_choice == 4:
            game_start = False
            progress_start = False
        else:
            print("\nInvalid input!")
            print("Please enter an integer value between 1 and 4.\n")
            print_card = False
            continue