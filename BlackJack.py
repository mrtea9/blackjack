from test import Deck, Hand, Chips

playing = True


def take_bet(player_chips):
    while True:
        try:
            bet = int(input("Make your bet: "))
            if bet > player_chips.total:
                print("You don't have enough chips! Try again.")
            else:
                player_chips.bet = bet
                break
        except ValueError:
            print("Sorry, a bet must be an integer. Please try again.")


def hit(deck, hand):
    hand.add_card(deck.deal_one())


def hit_or_stand(deck, hand):
    while True:
        choice = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if choice.lower() == 'h':
            hit(deck, hand)
            return True
        elif choice.lower() == 's':
            print("Player stands. Dealer is playing.")
            return False
        else:
            print("Sorry, please try again.")
            continue


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("Dealer's Hand =", dealer.cards[1].value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player_chips):
    player_chips.lose_bet()
    print("PLAYER IS BUSTED!")
    print("DEALER WINS!")


def player_wins(player_chips):
    player_chips.win_bet()
    print("PLAYER WINS!")


def dealer_busts(player_chips):
    player_chips.win_bet()
    print("DEALER IS BUSTED!")
    print("PlAYER WINS!")


def dealer_wins(player_chips):
    player_chips.lose_bet()
    print("DEALER WINS!")


def push():
    print("Dealer and Player tie! It's a push.")


def play_game():
    player_chips = Chips()

    while True:
        if player_chips.total == 0:
            print("GAME OVER!")
            break

        print("BLACKJACK AND SLIUHI!")

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        for _ in range(2):
            player_hand.add_card(deck.deal_one())
            dealer_hand.add_card(deck.deal_one())

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            playing = hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        print(f"\nPlayer's winnings stand at {player_chips.total}")
        new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() == 'n':
            print("Thanks for playing!")
            break
        else:
            continue


play_game()
