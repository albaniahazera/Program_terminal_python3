import termcolor, socket, program_for_pc1, ui, os
from termcolor import colored
from ui import welcomeUI
from games import gamespy

def main1():
    welcomeUI()
    print("\n\t\t\t\tPILIHAN PROGRAM\n")
    print(colored("[1] Alat", "green"))
    print(colored("[2] Game", "yellow"))
    user_option = int(input(colored("[0] Keluar \n\nPilih: ")))
    os.system("cls")
    if (user_option == 1):
        program_for_pc1.tools1()
    elif (user_option == 2):
        gamespy.game()
    elif (user_option == 0):
        exit()
        

if __name__ == "__main__":
    main1()    