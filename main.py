import cards_class
import time


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


deck1 = cards_class.Deck()
dealerHand = cards_class.Hand()
playerHand = cards_class.Hand()

deck1.shuffle()
dealerHand.cards.extend(deck1.deal(2))
playerHand.cards.extend(deck1.deal(2))
bust = False
win = False
print("Welcome to BlackJack!")
print("The dealer is currently showing %s" % (str(dealerHand.cards[1])))
print("============================================")
print("Your hand is: %s" % (playerHand.__str__()))
print("Your score is %s" % (score(playerHand.cards)))

# as long as no win or loss condition is met it will go through these actions
while bust == False and win == False:
    # Check if player wins and if so, finish game
    if score(playerHand.cards) == 21:
        print("Congratulations, you've won at Blackjack!!!!!")
        win = True
    # Check if the player busted, and if they did finish the game
    elif score(playerHand.cards) >= 21:
        print("It is my unfortunate privilege to tell you that you went bust and that means you lost the game.")
        bust = True
    # Loop for the player to hit or stand and then for the dealer to take his turn
    else:
        choice = input("Hit or Stand?\n")
        commands = ["hit", "stand"]
        while choice.lower() not in commands:
            choice = input("Hit or Stand?\n")
        if choice.lower() == "hit":
            playerHand.cards.extend(deck1.deal(1))
            print("You are dealt one card")
            print("Your hand is: %s" % (playerHand.__str__()))
            print("Your score is %s" % (score(playerHand.cards)))
        elif choice.lower() == "stand":
            dwin = False
            dbust = False
            print("The dealer shows his cards")
            # Loop for the dealer to take his turn, drawing until they have at least 17 and have not gone bust
            while dbust == False and dwin == False:
                time.sleep(1)
                print("The dealer's hand is: %s" % (dealerHand.__str__()))
                print("The dealer score is %s" % (score(dealerHand.cards)))
                # Dealer gets blackjack
                if score(dealerHand.cards) == 21:
                    time.sleep(1)
                    print("The dealer wins!  Hooray for the dealer! Boo for you though, you lost big time")
                    dwin = True
                    bust = True
                # Dealer goes bust
                elif score(dealerHand.cards) > 21:
                    time.sleep(1)
                    print("The dealer went bust.  Poor, poor dealer...Good for you though, you win!")
                    dbust = True
                    win = True
                else:
                    # Dealer draws
                    if score(dealerHand.cards) < 17 and score(dealerHand.cards) < score(playerHand.cards):
                        dealerHand.cards.extend(deck1.deal(1))
                        time.sleep(1)
                        print("The dealer has: %s" % (str(dealerHand)))
                    # Dealer stands
                    elif score(dealerHand.cards) >= 17 or score(dealerHand.cards) > score(playerHand.cards):
                        time.sleep(1)
                        print("The dealer stands")
                        print("The dealer's score is: %s" % (score(dealerHand.cards)))
                        print("Your score is: %s" % (score(playerHand.cards)))
                        if score(dealerHand.cards) > score(playerHand.cards):
                            time.sleep(1)
                            print("%d is bigger than %d, that means you're the big sad loser" % (
                            score(dealerHand.cards), score(playerHand.cards)))
                            dwin = True
                            bust = True
                        elif score(dealerHand.cards) < score(playerHand.cards):
                            time.sleep(1)
                            print(
                                "%d is bigger than %d, that means that dumb-dumb dealer lost the game, and you won!" % (
                                score(playerHand.cards), score(dealerHand.cards)))
                            win = True
                            dbust = True
                        elif score(dealerHand.cards) == score(playerHand.cards):
                            time.sleep(1)
                            print("You tied with the dealer.  That means the dealer wins, and you lose, unfair, "
                                  "but that's life")
                            dwin = True
                            bust = True
