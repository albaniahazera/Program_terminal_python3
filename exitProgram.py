import os, main, program_for_pc1 
from main import main1

def exitProgram1():
    input_out = input("\n\n\tApakah kamu yakin ingin kembali ke menu utama ? (y/n): ")
    os.system("cls")
    if input_out == "y":
        main1()

if __name__ == "__main__":
    exitProgram1()        