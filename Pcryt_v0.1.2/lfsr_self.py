# Client for LFSR encryption "Pcryt" modules
# @author dmimukto 2021

# MODULE IMPORTS
import sys
import pcryt_encryption
import os.path

# MAIN PROGRAM
def main():
    # selecting modes
    message = input("\n\nEnter message : ")
    print("what")
    if message=="_attemptall_":
        message = input("Enter message to decrypt : ")
        seed = input("Enter seed : ")
        seed_list = []
        taps = int(len(seed))
        for index in range(len(seed)):
            seed_list.append(bin(int(seed[index])))
        for trial in range(0,taps):
            cipher = pcryt_encryption.encrypt(message, seed_list, trial)
            print("For tap=", trial," output=",cipher)
            
    
    
    else:
        seed = input("Enter seed : ")
        seed_list = []
        taps = int(input("Enter tap position : "))
        for index in range(len(seed)):
            seed_list.append(bin(int(seed[index])))
        cipher = pcryt_encryption.encrypt(message,seed_list,taps)
        return print("\nEncrypted output : ",cipher)

    quitPrompt = input("Press ENTER to end.")
            
        

main()
    
