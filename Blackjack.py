from p1_random import P1Random
rng = P1Random()
game_continue = True
game_num = 0
player_wins = 0
tie = 0
dealer_wins = 0
#name = ""
# control the number of games the player will play how do i do that
while game_continue:
    game_num += 1
    print(f"START GAME #{game_num}")
    player_hand = 0
    card = rng.next_int(13) + 1
    name= card
    if card == 1:
        #print("ACE!")
        card = 11
        name = "ACE"
    elif 2 <= card <= 10:
        player_hand += card
        pass
    elif card == 11:
        #print("JACK!")
        card = 10
        name = "JACK"
    elif card == 12:
        #print("QUEEN!")
        card = 10
        name = "QUEEN"
    elif card == 13:
        #print("KING!")
        card = 10
        name = "KING!"

    no_winner = True
    while no_winner:
        print(f"Your card is a: {card}!")
        print(f"Your hand is: {player_hand}")
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit" + "\n")
        option = int(input("Choose an option:"))
        if option == 1:
            card = rng.next_int(13)+ 1
        if card == 1:
            #print("ACE!")
            card = 11
            print("ACE")
        elif 2 <= card <= 10:
            player_hand += card
            pass
        elif card == 11:
            #print("JACK!")
            card = 10
            name = "JACK"
        elif card == 12:
            #print("QUEEN!")
            card = 10
            name = "QUEEN"
        elif card == 13:
            #print("KING!")
            card = 10
            name = "KING"

            #calculate the players hand
            if player_hand == 21:
                print("winning message")
                no_winner = False
            elif player_hand == 21:
                if dealer_hand == 21:
                    print("It's a tie! No one wins!")
            elif player_hand > 21:
                print("losing message")
                no_winner = False
        elif option == 2:
            dealer_hand = rng.next_int(11) + 16
            if dealer_hand > 21:
                player_wins += 1
                print("Dealer's hand:", dealer_hand)
                print("Your hand is:", player_hand)
                print("You win!")
                pass
                # they lost, you win
            else:
                if player_hand > dealer_hand:
                    player_wins += 1
                    print("winning message")
                    pass
                    # won
                elif player_hand == dealer_hand:
                    tie += 1
                    print("It's a tie! No one wins!")
                    pass
                    # tie
                else:
                    dealer_wins += 1
                    print("losing message")
                    pass
                    # lost
            no_winner = False
        elif option == 3:
            print("Number of Player wins:", player_wins)
            print("Number of Dealer wins:", dealer_wins)
            print("Number of tie games:", tie)
            print("Total # of games played is:", game_num)
            print("Percentage of Player wins:", str(player_wins/ game_num * 100) + "%")
            # player wins, dealer wins, ties, total, % player wins
            print(str(player_hand) + str(dealer_wins))
            pass
        elif option == 4:
            no_winner = False
            game_continue = False
            break
        else:
            print("Please enter an integer value between 1 and 4")