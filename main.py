import sys
from time import sleep

Double_D = """   
                                                                 
88                                        88                     
88                                        88              ,d     
88                                        88              88     
88,dPPYba,  ,adPPYYba, 88,dPYba,,adPYba,  88  ,adPPYba, MM88MMM  
88P'    "8a ""     `Y8 88P'   "88"    "8a 8 a8P_____88   88     
88       88 ,adPPPPP88 88      88      88 88 8PP"""""""   88     
88       88 88,    ,88 88      88      88 88 "8b,   ,aa   88,    
88       88 `"8bbdP"Y8 88      88      88 88  `"Ybbd8"'   "Y888  

"""

for char in Double_D:
    sleep(0.5)
    sys.stdout.write(char)


class Ham_Game:
    def __init__(self):
        self.morality = 50
        self.sanity = 50
        self.relationships = {"Ophelia": 50, "Claudius": 50, "Gertrude": 50, "Horatio": 50}
        self.current_act = 1

    def start_game(self):
        print("Welcome to Hamlet's Game. Your choices will shape the story of Prince Hamlet.")
        input("Press Enter to begin your adventure...")
        self.act_one()

    def act_one(self):
        print("\nAct 1: The Ghost's Encounter")
        print("You encounter the ghost of your father, who reveals he was murdered by Claudius.")
        choice = input("Do you: (a) Vow to take revenge (b) Seek more information (c) Doubt the ghost\n")

        if choice == 'a':
            self.vow_revenge()
        elif choice == 'b':
            self.seek_information()
        elif choice == 'c':
            self.doubt_ghost()
        else:
            print("Invalid choice. Try again.")
            self.act_one()

    def vow_revenge(self):
        print("\nYou vow to take revenge against Claudius. This path darkens your heart but strengthens your resolve.")
        self.morality -= 10
        self.relationships["Claudius"] -= 20
        self.current_act = 2
        self.act_two()

    def seek_information(self):
        print("\nYou decide to gather more information before acting. Wisdom guides your path.")
        self.relationships["Horatio"] += 10
        self.current_act = 2
        self.act_two()

    def doubt_ghost(self):
        print("\nYou doubt the ghost's story. Is this madness or insight?")
        self.sanity += 5
        self.current_act = 2
        self.act_two()

    def act_two(self):
        print("\nAct 2: A Play Within a Play")
        print("You plan to stage a play that mirrors your father's murder to gauge Claudius's reaction.")
        choice = input("Do you: (a) Direct the play yourself (b) Ask Horatio for help (c) Abandon the plan\n")

        if choice == 'a':
            self.direct_play()
        elif choice == 'b':
            self.ask_horatio()
        elif choice == 'c':
            self.abandon_plan()
        else:
            print("Invalid choice. Try again.")
            self.act_two()

    def direct_play(self):
        print("\nYou take charge of the play. The court watches intently.")
        self.current_act = 3
        self.act_three()

    def ask_horatio(self):
        print("\nHoratio agrees to help with the play. His support bolsters your spirits.")
        self.relationships["Horatio"] += 10
        self.current_act = 3
        self.act_three()

    def abandon_plan(self):
        print("\nYou decide against the play. Perhaps there are other ways to uncover the truth.")
        self.current_act = 3
        self.act_three()

    def act_three(self):
        print("\nAct 3: The Confrontation")
        print("The tension in the court rises. You must now confront your own doubts and the suspicions of others.")
        choice = input("Do you: (a) Confront Claudius directly (b) Confide in Gertrude (c) Keep your plans secret\n")

        if choice == 'a':
            self.confront_claudius()
        elif choice == 'b':
            self.confide_in_gertrude()
        elif choice == 'c':
            self.keep_secrets()
        else:
            print("Invalid choice. Try again.")
            self.act_three()

    def confront_claudius(self):
        print("\nYou decide to confront Claudius, risking everything.")
        self.morality -= 5
        self.relationships["Claudius"] -= 30
        self.check_status()
        self.current_act = 4
        self.act_four()

    def confide_in_gertrude(self):
        print("\nYou turn to Gertrude for support. Does she trust you?")
        self.relationships["Gertrude"] += 15
        self.check_status()
        self.current_act = 4
        self.act_four()

    def keep_secrets(self):
        print("\nYou opt for secrecy, wondering your next move in solitude.")
        self.sanity -= 10
        self.check_status()
        self.current_act = 4
        self.act_four()

    def act_four(self):
        # Act 4 narrative and decisions
        pass

    def act_five(self):
        # Act 5 narrative and decisions, leading to the conclusion of the game
        pass

    def check_status(self):
        print("\nCurrent Status:")
        print(f"Morality: {self.morality}")
        print(f"Sanity: {self.sanity}")
        for character, relation in self.relationships.items():
            print(f"Relationship with {character}: {relation}")

# Start the game
game = Ham_Game()
game.start_game()

