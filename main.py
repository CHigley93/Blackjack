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


def evaluate(hand):
    if score(hand.cards) == 21:
        # Win
        return 1
    elif score(hand.cards) > 21:
        # Lose
        return 2
    else:
        # Continue
        return 3


deck1 = cards_class.Deck()
dealerHand = cards_class.Hand()
playerHand = cards_class.Hand()

deck1.shuffle()
dealerHand.cards.extend(deck1.deal(2))
playerHand.cards.extend(deck1.deal(2))
end = False
chosen = False
print("Welcome to BlackJack!")
print("The dealer is currently showing %s" % (str(dealerHand.cards[1])))
print("============================================")
print("Your hand is: %s" % (playerHand.__str__()))
print("Your score is %s" % (score(playerHand.cards)))

# as long as no win or loss condition is met it will go through these actions
while not end:
    # Check if player wins and if so, finish game
    if evaluate(playerHand) == 1:
        print("Congratulations, you've won at Blackjack!!!!!")
        end = True
    # Check if the player busted, and if they did finish the game
    elif score(playerHand.cards) >= 21:
        print("It is my unfortunate privilege to tell you that you went bust and that means you lost the game.")
        end = True
    elif playerHand.cards[0].rank == playerHand.cards[1].rank and chosen == False:
        choice = input("Would you like to split your hand?\n")
        commands = ["y", "yes", "n", "no"]
        while choice.lower() not in commands:
            choice = input("Would you like to split your hand?\n")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Ok we won't split your cards")
            chosen = True
        elif choice.lower() == "y" or choice.lower() == "yes":
            playerHand2 = cards_class.Hand()
            playerHand2.cards.extend(playerHand.pick_by_index(0))
            print("You split your hand")
            time.sleep(1)
            playerHand.cards.extend(deck1.deal(1))
            playerHand2.cards.extend(deck1.deal(1))
            print("Your first hand is %s with a score of %d" % (playerHand.__str__(), score(playerHand.cards)))
            time.sleep(1)
            print("Your second hand is %s with a score of %d" % (playerHand2.__str__(), score(playerHand2.cards)))
            time.sleep(1)
            print("We will play your first hand first")

            choice = input("Hit or Stand?\n")
            commands = ["hit", "stand"]
            while choice.lower() not in commands:
                choice = input("Hit or Stand?\n")
            # Player chooses to hit for 1st hand

                if choice.lower() == "hit":
                    playerHand.cards.extend(deck1.deal(1))
                    print("You are dealt one card")
                    print("Your first hand is: %s" % (playerHand.__str__()))
                    print("Your first hand score is %s" % (score(playerHand.cards)))
                    choice = ""
                # Player chooses to stand for 1st hand
                elif choice.lower() == "stand":

                    # Begin playing 2nd hand
                    print("Now we will play your second hand")
                    print("Your second hand is: %s" % (playerHand2.__str__()))
                    print("Your second hand score is %s" % (score(playerHand2.cards)))

                    choice = input("Hit or Stand?\n")
                    commands = ["hit", "stand"]
                    while choice.lower() not in commands:
                        choice = input("Hit or Stand?\n")

                    # Player chooses to hit for 2nd hand
                    if choice.lower() == "hit":
                        playerHand.cards.extend(deck1.deal(1))
                        print("You are dealt one card")
                        print("Your second hand is: %s" % (playerHand2.__str__()))
                        print("Your second hand score is %s" % (score(playerHand2.cards)))

                    # Player chooses to stand for 2nd hand
                    elif choice.lower() == "stand":

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
            print("The dealer shows his cards")
            # Loop for the dealer to take his turn, drawing until they have at least 17 and have not gone bust
            while not end:
                time.sleep(1)
                print("The dealer's hand is: %s" % (dealerHand.__str__()))
                print("The dealer score is %s" % (score(dealerHand.cards)))
                # Dealer gets blackjack
                if score(dealerHand.cards) == 21:
                    time.sleep(1)
                    print("The dealer wins!  Hooray for the dealer! Boo for you though, you lost big time")
                    end = True
                # Dealer goes bust
                elif score(dealerHand.cards) > 21:
                    time.sleep(1)
                    print("The dealer went bust.  Poor, poor dealer...Good for you though, you win!")
                    end = True
                else:
                    # Dealer draws
                    if score(dealerHand.cards) < 17:
                        time.sleep(1)
                        print("The dealer has: %s" % (str(dealerHand)))
                    # Dealer stands
                    elif score(dealerHand.cards) >= 17:
                        print("The dealer stands")
                        print("The dealer's score is: %s" % (score(dealerHand.cards)))
                        print("Your score is: %s" % (score(playerHand.cards)))
                        # Check if dealer has better hand
                        if score(dealerHand.cards) > score(playerHand.cards):
                            time.sleep(1)
                            print("%d is bigger than %d, that means you're the big sad loser" % (
                                score(dealerHand.cards), score(playerHand.cards)))
                            end = True
                        # Check if dealer has worse score
                        elif score(dealerHand.cards) < score(playerHand.cards):
                            time.sleep(1)
                            print(
                                "%d is bigger than %d, that means that dumb-dumb dealer lost the game, and you won!" % (
                                    score(playerHand.cards), score(dealerHand.cards)))
                            end = True
                        # Check for a draw
                        elif score(dealerHand.cards) == score(playerHand.cards):
                            time.sleep(1)
                            print("You tied with the dealer.  That means the dealer wins, and you lose, unfair, "
                                  "but that's life")
                            end = True
