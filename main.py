import cards_class
import time


# scoring method conforming to blackjack rules
def score(cards):
    total = 0
    aces = 0
    for card in cards:
        if 10 >= card.rank >= 2:
            total += card.rank
        elif 11 <= card.rank <= 13:
            total += 10
        elif card.rank == 1:
            aces += 1
    while aces > 0:
        if aces > 1:
            total += 1
            aces -= 1
        elif total <= 10:
            total += 11
            aces -= 1
        else:
            total += 1
            aces -= 1
    return total


# Starts the game by shuffling the deck, dealing 2 cards to the player and dealer, and displaying cards and score
def start_game(deck: cards_class.Deck, player: cards_class.Hand, dealer: cards_class.Hand):
    # deck.shuffle()
    player.cards.extend(deck.deal(2))
    dealer.cards.extend(deck.deal(2))
    print("The dealer is showing the {}".format(dealer.cards[1]))


def make_a_bet(money: int, betting_hand: cards_class.Hand):
    choice = "-1"
    while not (1 <= int(choice) <= money):
        choice = input("You have: {}\nWhat would you like to bet?\n".format(money))
        if not (1 <= int(choice) <= money):
            print("Not a valid choice")
        else:
            print("You bet: {}".format(int(choice)))
            betting_hand.wager = int(choice)
            money -= betting_hand.wager
            return money


def split_or_not(hand: cards_class.Hand, deck: cards_class.Deck, cash: int):
    if hand.cards[0].rank == hand.cards[1].rank and 2 * hand.wager <= cash:
        answers = ["yes", "no"]
        choice = ""
        while choice not in answers:
            print("Your hand is {} with a score of {}".format(hand.cards,score(hand.cards)))
            choice = input("Would you like to split your hand?\n")
            if choice.lower() == "yes":
                print("You split your hand")
                hand2 = cards_class.Hand()
                hand2.cards.extend(hand.pick_by_index(0))
                hand.cards.extend(deck.deal(1))
                hand2.cards.extend(deck.deal(1))
                hand2.wager = hand.wager
                print("Your new hands are {} with a score of {} and {} with a score of {}".format(
                    hand.__str__(), score(hand.cards), hand2.__str__(), score(hand2.cards)))
                return [hand, hand2], cash - hand.wager
            elif choice.lower() == "no":
                print("You do not split your hand")
                return [hand], cash
    else:
        return [hand], cash


def double_bet(hand: cards_class.Hand, cash: int, deck: cards_class.Deck):
    if hand.wager <= cash:
        print("You have {} with a score of {}".format(hand, score(hand.cards)))
        choice = ""
        options = ["yes", "no"]
        while choice.lower() not in options:
            choice = input("Would you like to double your hand?\n"
                           "You would double your bet of {} money to {} money\n".format(hand.wager,2*hand.wager))
            if choice.lower() == "yes":
                cash -= hand.wager
                print("You bet an additional {}".format(hand.wager))
                hand.wager *= 2
                time.sleep(3)
                print("Dealt one card")
                hand.cards.extend(deck.deal(1))
                print("You have {} with a score of {}".format(hand.__str__(), score(hand.cards)))
                if score(hand.cards) > 21:
                    print("Busted")
                return cash, True
            elif choice.lower() == "no":
                print("You do not double your hand")
                return cash, False
            else:
                continue
    else:
        return cash, False


# Allows the player to hit until bust or they choose to stand for 1 hand, returns True if they are still playing
# and False if they are Busted
def hit_or_stand(hand: cards_class.Hand, deck: cards_class.Deck):
    turn_over = False
    while not turn_over:
        print("You have {} with a score of {}".format(hand.__str__(), score(hand.cards)))
        choice = input("Hit or stand?\n")
        if choice.lower() == "hit":
            print("Dealt one card")
            hand.cards.extend(deck.deal(1))
            if score(hand.cards) > 21:
                print("Busted")
                turn_over = True
            else:
                continue
        elif choice.lower() == "stand":
            turn_over = True


# dealer hits until they are at 17 or higher
def dealer_play(hand: cards_class.Hand, deck: cards_class.Deck):
    end = False
    while not end:
        print("The dealer is showing {}".format(hand.__str__()))
        print("The dealer's score is {}".format(score(hand.cards)))
        if score(hand.cards) > 21:
            time.sleep(3)
            print("The dealer busts!")
            end = True
        elif score(hand.cards) > 17:
            time.sleep(3)
            print("The dealer stands")
            end = True
        else:
            time.sleep(3)
            print("The dealer hits")
            hand.cards.extend(deck.deal(1))


def score_check(player: cards_class.Hand, dealer: cards_class.Hand):
    print("The dealer has {} and his score is {}".format(dealer.__str__(), score(dealer.cards)))
    print("You have {} and your score is {}".format(player.__str__(), score(player.cards)))
    if score(player.cards) > 21:
        time.sleep(3)
        print("You lose {} money".format(player.wager))
        hand.wager = 0
    elif score(dealer.cards) > 21:
        time.sleep(3)
        print("You win {} money".format(player.wager))
        hand.wager *= 2
    elif score(player.cards) > score(dealer.cards):
        time.sleep(3)
        print("You win {} money".format(player.wager))
        hand.wager *= 2
    else:
        time.sleep(3)
        print("You lose {} money".format(player.wager))
        hand.wager = 0


def play_again(cash: int):
    # Check if player has money
    if cash <= 0:
        print("You are out of money.  Game over.")
        return False
    # asks if player wants to play again, returns false for yes and true for no
    choice = ""
    while choice.lower() not in ["yes", "no"]:
        choice = input("Would you like to play again?\n")
        if choice.lower() == "yes":
            return True
        elif choice.lower() == "no":
            return False


def discard_hand(hand: cards_class.Hand, deck: cards_class.Deck):
    for i in range(len(hand.cards) - 1, -1, -1):
        deck.cards.extend(hand.pick_by_index(i))


deck1 = cards_class.Hand()
for i in range(4):
    deck1.cards.extend(cards_class.Deck().cards)
deck1.shuffle()
dealer_hand = cards_class.Hand()
player_hand = cards_class.Hand()
replay = True
player_money = 500
player_hands = []

while replay:
    # Discard cards back into bottom of the deck
    for hand in player_hands:
        discard_hand(hand, deck1)
    discard_hand(dealer_hand, deck1)
    # ask for a bet
    player_money = make_a_bet(player_money, player_hand)
    # Setup hands for player and dealer
    start_game(deck1, player_hand, dealer_hand)
    busted = 0
    # Check for possible split
    player_hands, player_money = split_or_not(player_hand, deck1, player_money)
    # go through each hand until player doubles, busts or stands
    for hand in player_hands:
        double = False
        player_money, double = double_bet(hand, player_money, deck1)
        if not double:
            hit_or_stand(hand, deck1)
    # Calculate how many hands busted
    for hand in player_hands:
        if score(hand.cards) > 21:
            busted += 1
    # Check if there is at least one non busted hand
    if busted < len(player_hands):
        # Play the dealer's hand
        dealer_play(dealer_hand, deck1)
    # Check who won
    for hand in player_hands:
        score_check(hand, dealer_hand)
        player_money += hand.wager
    # ask to play again
    replay = play_again(player_money)

