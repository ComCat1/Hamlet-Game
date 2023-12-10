import sys
from time import sleep

Double_D = """ 
hamlet
                                                                                       | |
.----------------.  .----------------.  .----------------.  .----------------.         | |
| .--------------. || .--------------. || .--------------. || .--------------. |       | |
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | |       | |
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |       | |
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |       | |
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |       | | 
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |       | |
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |       | |
| |              | || |              | || |              | || |              | |       | |
| '--------------' || '--------------' || '--------------' || '--------------' |       | |
 '----------------'  '----------------'  '----------------'  '----------------'        | |  
                                                                                       | |
By: McKeane McBrearty AND Jackson Violich                                              | |
                                                                                       | |
________________________________________________________________________________________ /
"""

for char in Double_D:
    sleep(0.000001)
    sys.stdout.write(char)


class Game:
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
        print("\nAct 4: The conquest continues...")
        print("Polonius is dead. Gertrude has informed everyone of the news. Claudius wishes to send you to England. It is time to define your character.")
        choice = input("Do you: (a) Leave to England (b) Console Ophelia (c) Write a letter to horatio\n")

        if choice == 'a':
            self.leave_To_England()
        elif choice == 'b':
            self.console_Ophelia()
        elif choice == 'c':
            self.write_Letter()
        else:
            print("Invalid choice. Try again.")
            self.act_four()
    
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

    def act_five(self):
        print("\nAct 5: The Final Act")
        print("The endgame approaches. Your actions have shaped the course of events, and now you must face the consequences.")
        choice = input("Do you: (a) Challenge Claudius to a duel (b) Plan your escape (c) Seek reconciliation\n")

        if choice == 'a':
            self.challenge_claudius()
        elif choice == 'b':
            self.plan_escape()
        elif choice == 'c':
            self.seek_reconciliation()
        else:
            print("Invalid choice. Try again.")
            self.act_five()

    def challenge_claudius(self):
        print("\nYou challenge Claudius to a duel, facing your destiny head-on.")
        # Add logic for duel outcome based on player's current status
        self.conclude_game()

    def plan_escape(self):
        print("\nYou decide to flee, seeking a new life away from this tragedy.")
        # Add logic for escape outcome based on player's current status
        self.conclude_game()

    def seek_reconciliation(self):
        print("\nYou attempt to reconcile with those around you, seeking peace.")
        # Add logic for reconciliation outcome based on player's current status
        self.conclude_game()

    def conclude_game(self):
        # Summarize the player's journey and provide an ending based on their decisions
        print("\nYour journey as Hamlet has come to an end.")
        # Add logic to summarize the player's path and provide a fitting conclusion
        print("Thank you for playing!")

# Start the game
game = Game()
game.start_game()

#                   _ |\_   woof
#                   \` ..\  /
#              __,.-" =__Y=       woof
#            ."        )            \ ╱|、
#      _    /   ,    \/\_            (˚ˎ 。7  
#     ((____|    )_-\ \_-`            |、˜〵          
#      `-----'`-----` `--`            じしˍ,)ノ
