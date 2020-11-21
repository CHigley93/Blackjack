import cards_class
import time

deck1 = cards_class.Deck()
dealer_hand = cards_class.Hand()
player_hand = cards_class.Hand()
busted = 0


# scoring method conforming to blackjack rules
def score(cards):
    total = 0
    aces = 0
    for card in cards:
        if 11 > card.rank > 1:
            total += card.rank
        elif 10 < card.rank < 14:
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
    deck.shuffle()
    player.cards.extend(deck.deal(2))
    dealer.cards.extend(deck.deal(2))
    print("The dealer is showing the %s" % dealer.cards[1])
    print("Your hand is %s" % (player.__str__()))
    print("Your score is: %s" % (score(player.cards)))


def split_or_not(hand: cards_class.Hand, deck: cards_class.Deck):
    if hand.cards[0].rank == hand.cards[1].rank:
        answers = ["yes", "no"]
        choice = ""
        while choice not in answers:
            choice = input("Would you like to split your hand?\n")
            if choice.lower() == "yes":
                print("You split your hand")
                hand2 = cards_class.Hand()
                hand2.cards.extend(hand.pick_by_index(0))
                hand.cards.extend(deck.deal(1))
                hand2.cards.extend(deck.deal(1))
                print("Your new hands are %s with a score of %s and %s with a score of %s" % (
                    hand.__str__(), score(hand.cards), hand2.__str__(), score(hand2.cards)))
                return [hand, hand2]
            elif choice.lower() == "no":
                print("You do not split your hand")
                return [hand]
    else:
        return [hand]


# Allows the player to hit until bust or they choose to stand for 1 hand, returns True if they are still playing
# and False if they are Busted
def hit_or_stand(hand: cards_class.Hand, deck: cards_class.Deck):
    stood = False
    while not stood:
        print("You have %s with a score of %s" % (hand.__str__(), score(hand.cards)))
        choice = input("Hit or stand?\n")
        if choice.lower() == "hit":
            print("Dealt one card")
            hand.cards.extend(deck.deal(1))
            print("Your hand is %s" % (hand.__str__()))
            print("Your score is: %s" % (score(hand.cards)))
            if score(hand.cards) > 21:
                print("Busted")
            else:
                continue
        elif choice.lower() == "stand":
            stood = True


# dealer hits until they are at 17 or higher
def dealer_play(hand: cards_class.Hand, deck: cards_class.Deck):
    end = False
    while not end:
        print("The dealer is showing %s" % (hand.__str__()))
        print("The dealer's score is %s" % (score(hand.cards)))
        if score(hand.cards) > 21:
            time.sleep(1)
            print("The dealer busts!")
            end = True
        elif score(hand.cards) > 17:
            time.sleep(1)
            print("The dealer stands")
            end = True
        else:
            time.sleep(1)
            print("The dealer hits")
            hand.cards.extend(deck.deal(1))


def score_check(player: cards_class.Hand, dealer: cards_class.Hand):
    print("The dealer has %s and his score is %s" % (dealer.__str__(), score(dealer.cards)))
    print("You have %s and your score is %s" % (player.__str__(), score(player.cards)))
    if score(player.cards) > 21:
        time.sleep(1)
        print("You lose")
    elif score(dealer.cards) > 21:
        time.sleep(1)
        print("You win")
    elif score(player.cards) > score(dealer.cards):
        time.sleep(1)
        print("You win")
    else:
        time.sleep(1)
        print("You lose")


start_game(deck1, player_hand, dealer_hand)
player_hands = [player_hand]
player_hands = split_or_not(player_hand, deck1)
for hand in player_hands:
    hit_or_stand(hand, deck1)
for hand in player_hands:
    if score(hand.cards) > 21:
        busted += 1
if busted < 2:
    dealer_play(dealer_hand, deck1)
for hand in player_hands:
    score_check(hand, dealer_hand)
