# Client for LFSR encryption "Pcryt" modules
# @author dmimukto 2021

# MODULE IMPORTS
import sys
import pcryt_encryption
import os.path

# MAIN PROGRAM
def main():
    message = sys.argv[1]
    if message=="attemptall":
        message = input("Enter message to decrypt : ")
        seed = sys.argv[2]
        seed_list = []
        taps = len(seed)
        for index in range(len(seed)):
            seed_list.append(bin(int(seed[index])))
        for trial in range(0,taps):
            cipher = pcryt_encryption.encrypt(message, seed_list, trial)
            print("For tap=", trial," output=",cipher)
            
    
    
    else:
        seed = sys.argv[2]
        seed_list = []
        taps = int(sys.argv[3])
        for index in range(len(seed)):
            seed_list.append(bin(int(seed[index])))
        cipher = pcryt_encryption.encrypt(message,seed_list,taps)
        return print(cipher)
            
        

main()
    
