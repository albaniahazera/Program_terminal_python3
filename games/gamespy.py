import random, os, socket, termcolor, exitProgram
from termcolor import colored
        

def game():    
    def game1():
        while True:
            bentuk_goa = "|_|"
            goa_kosong = [bentuk_goa] * 6
            tikus = random.randint(1, 6)
            goa = goa_kosong.copy()
            goa[tikus - 1] = "|0_0|"
            goa_kosong = ' '.join(goa_kosong)
            goa = ' '.join(goa)
            print(colored("\n\t[Tebak tempat tikus bersembunyi]", "yellow"))
            print(colored(f"\nperhatikan goa dibawah ini \n\n{goa_kosong}\n", "yellow"))
            pilihan_user = int(input(colored("Menurut kamu dimana tikus berada? (1/2/3/4/5/6): ", "yellow")))
            if pilihan_user == tikus:
                print(colored(f"\n{goa}\n\nSelamat Kamu Menang Tikus Berada DI Goa Nomor {tikus} !", "yellow"))
            else:
                print(colored(f"\n{goa}", "yellow"))
                print(colored(f"\n\nKamu Salah Tikus Berada Di Goa Nomor {tikus} !", "red"))
            main_lagi = input("\n\n[Apakah ingin melanjutkan gamenya lagi ? (y/n)]: ")
            os.system("cls")
            if main_lagi == "n":
                break    

    while True:
        print(colored(("#" * 63), 'green'))
        nama = colored("ALZ", "red")
        title = ("(masih dalam pengembangan)")
        title1 = colored("]       # ", "green")
        title2 = colored("!HANYA UNTUK KEGUNAAN PRIBADI!", "red")
        title3 = colored("#", "green")
        title4 = colored("Versi 0.0.1[03]", "white")
        title5 = colored("#", "green")
        print(colored(f"#\t[ PROGRAM OLEH {nama} {title} {title1}", "green"))
        print(colored("#\t-----------------------------------------------       # ", "green"))
        print(colored(f"#\t        {title2}                {title3} ", "green"))
        print(colored("#\t        ------------------------------                # ", "green"))
        print(colored(f"#\t              {title4}                         {title5}", "green"))
        print(colored(("#" * 63) ,"green")) 
        print(colored("\n\nPILIHAN", "yellow"))
        print(colored("\n1. Tebak tempat tikus bersembunyi", "yellow"))
        userinput = int(input("0. Keluar \n\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            game1()
        elif (userinput == 0):
            exitProgram.exitProgram1()

if __name__ == "__main__":
    game()    