import random
import os
from blackjack_assets import logo

DECK = [11,2,3,4,5,6,7,8,9,10,10,10,10]


class Player():
    def __init__(self):
        self.cards = self.get_cards()
        self.total = self.get_total()
        self.status = "N/A"

    def get_cards(self):
        return [random.choice(DECK),random.choice(DECK)]
    
    def add_a_card(self):
        self.cards.append(random.choice(DECK))
        self.total = self.get_total()

    def get_total(self):
        if 11 in self.cards:
            ace_calc = sum(self.cards)
            eleven_count = self.cards.count(11)
            for i in range(eleven_count):
                if ace_calc > 21:
                    ace_calc -= 10
                else:
                    break
            
            return ace_calc
        else:
            return sum(self.cards)

    def choice(self):
        return input("Type 'y' to get another card, type 'n' to pass: ")
    
    def final_hand(self):
        print(f"    Your final hand: {self.cards}, final score: {self.total}")
        if self.status == "BLACKJACK":
            print(f"    Computer's final hand: {dealer.cards[0]}, final score: {dealer.cards[0]}")
        else:
            print(f"    Computer's final hand: {dealer.cards}, final score: {dealer.total}")
    
    def reset(self):
        self.cards = self.get_cards()
        self.total = sum(self.cards)
        self.status = "N/A"
    
class Dealer(Player):
    def __init__(self):
        super().__init__()
    
    def compute_final_score(self):
        checking = True
        while checking:
            if self.total > 21:
                player.status = "WIN"
                checking = False
            elif self.total == 21 or (player.total < self.total and self.total < 21):
                player.status = "LOSE"
                checking = False
            elif player.total > self.total and self.total < 17 or player.total == 21:
                self.add_a_card()
            elif player.total == self.total:
                player.status = "DRAW"
                checking = False
            elif player.total == 21:
                player.status = "BLACKJACK"
                checking = False
            
        
def game_reset(player,dealer):
    player.reset()
    dealer.reset()
    
def main():
    
    running = True
    while running:
        os.system("cls")
        print(logo)
        
        print(f"    Your cards: {player.cards}, current score: {player.total}")
        print(f"    Computer's first card: {dealer.cards[0]}")
        if player.total < 21:
            choice = player.choice()
            if choice == "y":
                player.add_a_card()
            elif choice == "n":
                dealer.compute_final_score()
                player.final_hand()
                running = False
        elif player.total == 21:
            dealer.compute_final_score()
            player.final_hand()
            running = False
        elif player.total > 21:
            player.status = "LOSE"
            player.final_hand()
            running = False
        

if __name__ == "__main__":
    player = Player()
    dealer = Dealer()
    while True:
        begin_game = input("Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()
        if begin_game == "y":
            main()
            if player.status == "BLACKJACK":
                print("Win with a Blackjack!")
            elif player.status == "WIN":
                print("You WON!")
            elif player.status == "DRAW":
                print("Game ended in a Draw.")
            elif player.status == "LOSE":
                print("You LOSE!")
                
            game_reset(player,dealer)
        else:
            break
