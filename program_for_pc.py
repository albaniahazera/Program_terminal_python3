import os, random, string, pyperclip, termcolor, math, sys, socket
from termcolor import colored

def penghitung():
    def pertambahan():
        print(colored("\n\t*PERTAMBAHAN*", "blue"))
        jumlah = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah == "":
            jumlah = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah1 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah1 == "":
            jumlah1 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah2 = float(jumlah)
        jumlah3 = float(jumlah1)
        hasil = (jumlah2) + (jumlah3)
        hasil1 = str(hasil) 
        print(colored("\nHasil: " + hasil1, "blue" ))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke pertambahan \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pertambahan()    

    def pengurangan():
        print(colored("\n\t*PENGURANGAN*", "blue"))
        jumlah2 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah2 == "":
            jumlah2 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah3 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah3 == "":
            jumlah3 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah4 = float(jumlah2)
        jumlah5 = float(jumlah3)
        hasil1 = (jumlah4) - (jumlah5)
        hasil2 = str(hasil1)
        print(colored("\nHasil: " + hasil2, "blue" ))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke pengurangan \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pengurangan()

    def perkalian():
        print(colored("\n\t*PERKALIAN*", "blue"))
        jumlah4 = input(colored("\nMasukkan  Angka: ", "blue"))
        while jumlah4 == "":
            jumlah4 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah5 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah5 == "":    
            jumlah5 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah6 = float(jumlah4)
        jumlah7 = float(jumlah5)    
        hasil2 = (jumlah6) * (jumlah7)
        hasil3 = str(hasil2)
        print(colored("\nHasil: " + hasil3, "blue" ))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke perkalian \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            perkalian()

    def pembagian():
        print(colored("\n\t*PEMBAGIAN*", "blue"))
        jumlah6 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah6 == "":
            jumlah6 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah7 = input(colored("\nMasukkan Angka: ", "blue"))
        while jumlah7 == "":
            jumlah7 = input(colored("\nMohon Masukkan Angka: ", "blue"))
        jumlah8 = float(jumlah6)
        jumlah9 = float(jumlah7)    
        hasil3 = (jumlah8) / (jumlah9)
        hasil4 = str(hasil3)
        print(colored("\nHasil: " + hasil4, "blue")) 
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke pembagian \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pembagian()

    def waktu():
        print(colored("\t*PENGHITUNG DETIK*", "blue"))
        detik = input(colored("\nMasukkan detik: ", "blue"))
        while detik == "":
            detik = input(colored("\nMohon Masukkan Detik: ", "blue"))
        detik1 = eval(detik)    
        jam = detik1 // 3600
        detik1 = detik1 % 3600
        menit = detik1 // 60
        detik1 = detik1 % 60
        print(colored(f"\nHasil:  {jam} Jam {menit} Menit {detik1} Detik", "blue" ))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke penghitung waktu \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            waktu()

    def derajat():
        def fahrenheit():
            print(colored("\t*PENGHITUNG DERAJAT DARI FAHRENHEIT KE CELCIUS*", "blue"))
            derajatf = input(colored("\nMasukkan suhu fahrenheit (HANYA ANGKA): ", "blue"))
            while derajatf == "":
                derajatf = input(colored("\nMohon masukkan suhu fahrenheit (HANYA ANGKA): ", "blue"))
            derajatf1 = eval(derajatf)
            derajatc = 5/9*(derajatf1 - 32)
            print(colored(f"\nHasil: {derajatf1} Derajat Fahrenheit =  {derajatc} Derajat Celcius", "blue"))
            userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke penghitung fahrenheit ke celcius \n0.Keluar \n\nPilih: ", "blue")))
            os.system("cls")
            if (userinput == 1):
                fahrenheit()

        def celcius():
            print(colored("\t*PENGHITUNG DERAJAT DARI CELCIUS KE FAHRENHEIT *", "blue"))
            derajatc = input(colored("\nMasukkan suhu celcius (HANYA ANGKA): ", "blue"))
            while derajatc == "":
                derajatc = input(colored("\nMohon masukkan suhu celcius (HANYA ANGKA): ", "blue"))
            derajatc1 = eval(derajatc)
            derajatf = (9/5 * derajatc1 )+ 32
            print(colored(f"\nHasil: {derajatc1} Derajat Celcius =  {derajatf} Derajat Fahrenheit", "blue"))
            userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke penghitung celcius ke fahrenheit \n0.Keluar \n\nPilih: ", "blue")))
            os.system("cls")
            if (userinput == 1):
                celcius()
        
        while True:
            print(colored("\n\t[PENGHITUNG SUHU] ", "blue"))
            print(colored("\n\nPILIHAN ", "blue"))
            print(colored("\n1.Fahrenheit ke celcius ", "blue"))
            print(colored("2.Celcius ke fahrenheit ", "blue"))
            userinput = int(input("0.Keluar \n\nPilih: "))
            os.system("cls")
            if (userinput == 1):
                fahrenheit()
            elif (userinput == 2):
                celcius()
            else:
                break        

    while True:
        print(colored("\n\t[PENGHITUNG] \n\nPILIHAN", "blue"))
        print(colored("\n1.Pertambahan", "blue"))
        print(colored("2.Pengurangan", "blue"))
        print(colored("3.Perkalian", "blue"))
        print(colored("4.Pembagian", "blue"))
        print(colored("5.Penghitung detik", "blue"))
        print(colored("6.Penghitung suhu", "blue"))
        print(colored("0.Keluar"))
        userinput = int(input("\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            pertambahan()
        elif (userinput == 2):
            pengurangan()
        elif (userinput == 3):
            perkalian()
        elif (userinput == 4):
            pembagian()
        elif (userinput == 5):
            waktu()
        elif (userinput == 6):
            derajat()        
        else:
            break                


def pembalik():
    def pembalikkata():
        print(colored("\t*PEMBALIK KATA*", "blue"))
        pesan = str(input(colored("\nMasukkan kata: ", "blue"))) 
        ubah = ""
        i = len(pesan)-1
        while i >= 0:
            ubah = ubah + pesan[i]
            i = i -1
        print(colored(f"\nHasil kata yang dibalik:  {ubah}", "blue"))    
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke program pembalik kata \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pembalikkata()

    def mengembalikkankata():
        print(colored("\t*MENGEMBALIKKAN KATA YANG DIBALIK*", "blue"))
        pesan = str(input(colored("\nMasukkan kata: ", "blue"))) 
        ubah = ""
        i = len(pesan)-1
        while i >= 0:
            ubah = ubah + pesan[i]
            i = i -1
        print(colored(f"\nHasil kata yang dikembalikan:  {ubah}", "blue"))    
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke program mengembalikkan kata yang dibalik \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            mengembalikkankata()

    while True:
        print(colored("\n\t[PEMBALIK KATA]", "blue"))
        print(colored("\nPILIHAN", "blue"))
        print(colored("\n1.Pembalik kata ", "blue"))
        print(colored("2.Mengembalikan kata yang dibalik ", "blue"))
        userinput = int(input("0.Keluar \n\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            pembalikkata()
        elif (userinput == 2):
            mengembalikkankata()    
        else:
            break  


morse_dict = {
    'A':".-", 'B':"-...", 'C':"-.-.", 'D':"-..", 'E':".", 'F':"..-.", 'G':"--.", 'H':"....", 'I':"..", 'J':".---", 'K':"-.-", 'L':".-..", 'M':"--", 'N':"-.", 'O':"---", 'P':".--.", 'Q':"--.-", 'R':".-.", 'S':"...", 'T':"-", 'U':"..-", 'V':"...-", 'W':".--", 'X':"-..-", 'Y':"-.--", 'Z':"--..", '1':".----", '2':"..---", '3':"...--", '4':"....-", '5':".....", '6':"-....", '7':"--...", '8':"---..", '9':"----.", '0':"-----", ',':"--..--", '.':".-.-.-", '?':"..--..", '/':"-..-.", '-':"-....-", '(':"-.--.", ')':"-.--.-"}


def morse():
    def encrypt(pesan):
        cipher = ''
        for kata in pesan:
          if kata != ' ':
            cipher += morse_dict[kata]
          else:
            cipher += ' '    
        return cipher 

    def decrypt(pesan):
        pesan += ' '
        decipher = ''
        citext= ''
        for kata in pesan:
          if (kata != ' '):
            i = 0
            citext += kata
          else:
              i += 1

              if i == 2:
                 decipher += ' '
              else:
                 decipher += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                 citext = ''
        return decipher          

    def main1():
        print(colored("\n\t[KODE MORSE]", "blue"))
        pesan = str(input(colored("\nMasukkan huruf: ", "blue")))
        result = encrypt(pesan.upper())
        print(colored(f"\nHasil: {result}", "blue"))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke program, Dari alphabet ke morse \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            main1()
        
    def main2():
        print(colored("\n\t[KODE MORSE]", "blue"))
        pesan = str(input(colored("\nMasukkan kode morse satu persatu (AGAR TIDAK TERJADI ERROR): ", "blue")))
        result = decrypt(pesan) 
        print(colored(f"\nHasil:  {result}", "blue"))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Kembali ke program, Dari morse ke alphabet \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            main2()

    while True:
       print(colored("\n\t[KODE MORSE]", "blue"))
       print(colored("\nPILIHAN", "blue"))
       print(colored("\n1.Alphabet ke morse ", "blue"))
       print(colored("2.Morse ke alphabet", "blue"))
       userinput = int(input("0.Keluar \n\nPilih: "))
       os.system("cls")
       if (userinput == 1):
          main1()
       elif (userinput ==2):
          main2()
       else:
          break


def password():
    def pembuatpassword():
        angka = ["1","2","3","4","5","6","7","8","9","0"]
        huruf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        print(colored("\t*PEMBUAT PASSWORD PENDEK*", "blue"))
        angka1 = random.choice(angka)
        huruf1 = random.choice(huruf)
        number = random.randrange(0, 101)
        special_char = random.choice(string.punctuation)
        password1 = angka1 + huruf1 + str(number) + special_char
        print(colored(f"\nHasil password: {password1}", "blue"))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Buat lagi password pendek \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pembuatpassword()

    def pembuatpassword1():
        angka = ["123","234","345","456","567","678","789","8910","91011","01112"]
        huruf = ["AB","BC","CD","DE","EF","FG","GH","HI","IJ","JK","KL","LM","MN","NO","OP","PQ","QR","RS","ST","TU","UV","VW","WX","XY","YZ","ZA"]
        print(colored("\t*PEMBUAT PASSWORD PANJANG*", "blue"))
        angka1 = random.choice(angka)
        huruf1 = random.choice(huruf)
        number = random.randrange(0, 101)
        special_char = random.choice(string.punctuation)
        password1 = angka1 + huruf1 + str(number) + special_char
        print(colored(f"\nHasil password: {password1}","blue"))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Buat lagi password panjang \n0.Keluar \n\nPilih: ", "blue")))
        os.system("cls")
        if (userinput == 1):
            pembuatpassword1()

    while True:
        print(colored("\n\t[PEMBUAT PASSWORD]", "blue"))
        print(colored("\nPILIHAN", "blue"))
        print(colored("\n1.Password pendek", "blue"))
        print(colored("2.Password panjang", "blue"))
        userinput = int(input("0.Keluar \n\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            pembuatpassword()
        elif (userinput == 2):
            pembuatpassword1()
        else:
            break  


def sandi_caesar():
    def sandi_caesar_in():
       print(colored("\n\t*SANDI CAESAR*", "green"))
       pesan = str(input(colored("\n\nMasukkan pesan: ", "green"))) 
       kunci = 13
       mode = 'encrypt' 
       HURUF ='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
       ubah = ''
       pesan = pesan.upper() 
       for symbol in pesan: 
          if symbol in HURUF: 
             nomor = HURUF.find(symbol) 
             if mode == 'encrypt': 
                nomor = nomor + kunci 
             elif mode == 'decrypt': 
                nomor = nomor - kunci
             if nomor >= len(HURUF): 
                nomor = nomor - len(HURUF) 
             elif nomor < 0: 
                nomor = nomor + len(HURUF)     
             ubah = ubah + HURUF[nomor] 
          else:     
             ubah = ubah + symbol
       print(colored(f'Hasil:  {ubah}', "green"))
       pyperclip.copy(ubah)
       userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Buat lagi sandi caesar \n0.Keluar \n\nPilih: ", "green")))
       os.system("cls")
       if (userinput == 1):
            sandi_caesar_in()    
    
    while True:
       print(colored("\n\t[PEMBUAT SANDI CAESAR]", "green"))
       print(colored("\n\nPILIHAN", "green"))
       print(colored("\n1.Buat sandi caesar", "green"))
       userinput = int(input("0.Keluar \n\nPilih: "))
       os.system("cls")
       if (userinput == 1):
           sandi_caesar_in()
       else:
           break   

def pesantransposisi():
    def main():
        def main1():
            print(colored("\n\t*ENKRIPSI PESAN TRANSPOSISI*", 'green'))        
            pesanSaya = input(colored("\nMasukkan pesan: ", 'green'))
            kunciSaya = 8
            sanditeks = enkripsiPesan(kunciSaya, pesanSaya)
            print(colored(f"\nHasil:  {sanditeks}", "green"))
            pyperclip.copy(sanditeks)
            userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Enkripsi lagi pesan transposisi \n0.Keluar \n\nPilih: ", "green")))
            os.system("cls")
            if (userinput == 1):
                main1()

        def enkripsiPesan(kunci, pesan):
            sanditeks = [''] * kunci
            for col in range(kunci):
                pointer = col
                while pointer < len(pesan):
                    sanditeks[col] += pesan[pointer]
                    pointer += kunci
            return ''.join(sanditeks)
        if __name__ == '__main__':
            main1()
    
    def main1():    
        def main2():
            print(colored("\n\t*DEKRIPSI PESAN TRANSPOSISI*", 'green'))
            pesanSaya = input(colored("\nMasukkan pesan: ", 'green'))
            kunciSaya = 8
            teksawal = dekripsiPesan(kunciSaya, pesanSaya)
            print(colored(f"\nHasil:  {teksawal}", "green"))
            pyperclip.copy(teksawal)
            userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Dekripsi lagi pesan transposisi \n0.Keluar \n\nPilih: ", "green")))
            os.system("cls")
            if (userinput == 1):
                main2()
    

        def dekripsiPesan(kunci, pesan):
            jumlahKolom = math.ceil(len(pesan) / kunci)
            jumlahBaris = kunci
            jumlahKotakyangTerisi = (jumlahKolom * jumlahBaris) - len(pesan)
            teksawal = [''] * jumlahKolom
            kolom = 0
            baris = 0
            for symbol in pesan:
                teksawal[kolom] += symbol
                kolom += 1
                if (kolom == jumlahKolom) or (kolom == jumlahKolom - 1 and baris >=jumlahBaris - jumlahKotakyangTerisi):
                    kolom = 0
                    baris += 1
            return''.join(teksawal)
        if __name__=='__main__':
            main2()    

    while True:
        print(colored("\n\t[PESAN TRANSPOSISI]", 'green'))        
        print(colored("\n\nPILIHAN", 'green'))
        print(colored("\n1.Masuk ke enkripsi pesan", 'green'))
        print(colored("2.Masuk ke dekripsi pesan", 'green'))
        userinput = int(input("0.Keluar \n\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            main()
        elif (userinput == 2):
            main1()
        else:
            break

def brute_force():
    def brute_force_in():
        print(colored("\n\t*BRUTE FORCE*", "green"))
        pesan = str(input(colored("\nMasukkan pesan: ", "green")))
        HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for kunci in range(len(HURUF)): 
            ubah = ''
            for symbol in pesan: 
                if symbol in HURUF:
                    nomor = HURUF.find(symbol) 
                    nomor = nomor - kunci
                    if nomor < 0: 
                        nomor = nomor + len(HURUF)
                    ubah = ubah + HURUF[nomor] 
                else:  
                    ubah = ubah + symbol 
            print(colored('Hasil #%s: %s' % (kunci, ubah), "green"))
        userinput = int(input(colored("\nPILIHAN------------------------------------------------- \n\n1.Pecahkan lagi pesan/sandi dengan brute force \n0.Keluar \n\nPilih: ", "green")))
        os.system("cls")
        if (userinput == 1):
            brute_force_in()

    while True:
        print(colored("\n\t[BRUTE FORCE] ", "green"))
        print(colored("\n\nPILIHAN ", "green"))
        print(colored("\n1.Pecahkan pesan/sandi dengan brute force ", "green"))
        userinput = int(input("0.Keluar \n\nPilih: "))
        os.system("cls")
        if (userinput == 1):
            brute_force_in()
        else:
            break


def lainnya():
    def masuk():
        print(colored("\t[BERHASIL MASUK]", "red"))
        print("\n\n1) .--..-.--..-..-.-...--.-.-..- \n\n2) -.-..--...--..-... .-....-.--. \n\n3) -....--....--.-..- \n\n0) -.-..-....-.-.-.")
        def satu():
            print("Hai namaku adalah Albania Hazera aku berumur 19 tahun pada 2024, aku sedang membuat program milikku sendiri, aku berjanji aku harus bisa menciptakan program terbaik semasa hidupku agar aku bisa dikenang oleh banyak orang karena program buatanku")
            print("\n\n2) -.-..--...--..-... .-....-.--. \n\n0) -.-..-....-.-.-. ") 
        def dua():
            print("NXH ZRENFN FRCREGV BENAT LNAT TNTNY, NXH FRYNYH ORECVXVE ONUJN NXH XNYNU QNYNZ FRTNYNALN FRUVATTN NXH ZRENFNXNA XRFRQVUNA LNAT GNX NQN URAGVALN, NXH GNXHG ONUJN NCN LNAT FNNG VAV NXH XREWNXNA QNA CRYNWNEV GVQNX NEGVALN QV ZNFN QRCNA QRATNA XNGN YNVA NXH TNTNY NGNH NXH GREYNYH PRCNG ZRAVATTNYXNA QHAVN VAV FRUVATTN NXH GVQNX OVFN ZRYNAWHGXNA QNA ZRATRZONATXNA CEBTENZ VAV, QNA NXH GNXHG FRORYHZ NXH FHXFRF XRQHN BENAT GHNXH FHQNU GVNQN, NXH YROVU GNXHG UNY VAV QNEV CNQN UNY YNVAALN WVXN UNY VGH GREWNQV NXH GNX GNH VATVA OREXNGN NCN YNTV, NXH ENFN XRZNGVNAXH WNHU YROVU ONVX QNEV CNQN NXH UNEHF ZRYVUNG BENAT GHN NGNH XRYHNETNXH ZRAVATTNYXNAXH GREYROVU QNUHYH, GNCV CNQN FNNG VAV FNNG ZRAHYVF VAV NXH ZRENFN ZNFVU ZRZCHALNV QBEBATNA LNAT ORFNE HAGHX ZRAWNQV BENAT LNAT FHXFRF QNA NXH OREUNENC WVXN NXH FHXFRF FHNGH FNNG ANAGV NXH VATVA XRQHN BENAT GHNXH QNA XRYHNETNXH OVFN ZRYVUNGALN UNALN VGH UNENCNAXH.")
            print("\n\n[tt ka eadanfksin os p br bedrcdiceueisantaahge]")
            print("\n\n3) -....--....--.-..- \n\n0) -.-..-....-.-.-. ")         
        def tiga():
            print("HAGHX QHAVN, NXH ZRENFN QHAVN VAV OHXNA GRZCNG LNAT NZNA QNEV FRTNYN NAPNZNA FRCREGV XRZNGVNA QNA UNY YNVAALN, QVQHAVN VAV XNZH QNCNG ZRENFNXNA NCN FNWN FRCREGV XRFRQVUNA, XRXRFNYNA, XRFRANATNA, QNA LNAT YNVAALN, GRGNCV HAGHX QHAVN NXH ZRENFN QHAVN YROVU ONALNX ZRATNAQHAT ENFN FRQVU QRATNA XNGN YNVA QVQHAVN VAV FRZHN ZNXUYHX UVQHC GVQNX XRXNY FRZHN LNAT UVQHC NXNA ZRENFNXNA XRZNGVNA QNA BENAT NGNH ZNXUYHX YNVAALN LNAT QVGVATTNY NXNA ZRENFNXNA XRFRQVUNA LNAT ZRAQNYNZ, UNY VAV GVQNX UNALN GREWNQV CNQN FRFNZN ZNAHFVN GRGNCV OVFN WHTN ZNAHFVN GREUNQNC URJNA NGNH FRONYVXALN, NXH QVGVATTNY BYRU XHPVATXH LNAT OREANZN RCVA NXH FNATNG ZRALNLNATVALN GRGNCV CNQN FHNGH UNEV QVN FNXVG QNA GVQNX ZNH ZNXNA FNZCNV ORORENCN UNEV YNYH FRGRYNU ORORENCN UNEV OREYNYH QVN CRETV GVQNX CREANU XRZONYV FNZCNV FNNG VAV NXH ENFN QVN FHQNU GVQNX NQN QRATNA XNGN YNVA FHQNU ZNGV NXH QNCNG ZRATNFHZFVXNAALN XNERAN QVN FHQNU FNXVG FNXVGNA QNA GVQNX ZNH ZNXNA FNZN FRXNYV, NXH ZRENFN TNTNY QNYNZ ZRENJNGALN CNQNUNY XHPVAT VGH NXH LNAT ZRZONJNALN XR EHZNU GNCV NXH ZNYNU TNTNY ZRZOHNG HZHEALN YROVU YNZN NXH ZNYNU ZRZOVNEXNAALN CRETV ORTVGH FNWN QNA ZRAVATTNYXNAXH HAGHX FRYNZNALN, NXH ZREVAQHXNAZH NXH UNENC NXH OVFN ZRYVUNGZH HAGHX LNAT GRENXUVE XNYVALN NTNE NXH OVFN GRANAT, HAGHXZH RCVA.")
            print("\n\n[tt ka eadanfksin os p br bedrcdiceueisantaahge]")
            print("\n\n1) .--..-.--..-..-.-...--.-.-..- \n\n0) -.-..-....-.-.-. ")


        while True:
            userinput = int(input("\n\n.--....-........: "))
            os.system("cls") 
            if (userinput == 1):
                satu()
            elif (userinput == 2):
                dua()
            elif (userinput == 3):
                tiga()          
            else:
                break            
    
    while True:
        print(colored("\n\n\t*_* KAMU MEMASUKI PROGRAM RAHASIA *_* ", "red"))
        print(colored("\n\n\t\t[UNTUK MEMBUKA] ", "red"))
        print(colored("\n\n--.-.....--.- .--..-.-----..-..--- "))
        userinput = str(input(colored('\n\nMasukkan arti kode morse diatas dengan huruf kecil: ', "red")))
        os.system("cls")
        if (userinput == "masuk program"):
            masuk()
        else:
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
    device_name = socket.gethostname()
    print(colored(f"\n----------------- Devicemu: {device_name} --------------------------\n", "light_cyan"))
    print(colored("***************************************************************", "green"))
    print(colored("1.Penghitung", "blue"))
    print(colored("2.Pembalik Kata", "blue"))
    print(colored("3.Kode Morse", "blue"))
    print(colored("4.Pembuat Password", "blue"))
    print(colored("5.Pembuat Sandi caesar", "green"))
    print(colored("6.Pesan Transposisi", "green"))
    print(colored("7.Brute Force", "green"))
    print(colored("0.Keluar"))
    print(colored("***************************************************************", "green"))
    print(colored("\n--.-.....--.--.-.--. .--.--.-.-.- ----.----. .---..-.-. --.---.....--.-.- .--..-.-----..-..--- .-..-.....-......-", "red"))
    userinput = int(input("\n\npilih: "))
    os.system("cls") 
    if (userinput == 1):
        penghitung() 
    elif (userinput == 2):
        pembalik()    
    elif (userinput == 3):
        morse()    
    elif (userinput == 4):
        password()    
    elif (userinput == 5):
        sandi_caesar()
    elif (userinput == 6):
        pesantransposisi()
    elif (userinput == 7):
        brute_force()
    elif (userinput == 0):
        input_out = input("\n\n\tApakah kamu yakin ingin keluar program ? (y/n): ")
        os.system("cls")
        if input_out == "y":
            break            
    elif (userinput == 99):
        lainnya()    
    else:
        break    

