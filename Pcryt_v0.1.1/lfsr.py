# Client for LFSR encryption "Pcryt" modules
# @author dmimukto 2021

# MODULE IMPORTS
import sys
import pcryt_encryption

# MAIN PROGRAM
def main():
    message = sys.argv[1]
    taps = int(sys.argv[2])
    # seed generation (default)
    seed = []
    seed.append(bin(1))
    seed.append(bin(0))
    seed.append(bin(0))
    seed.append(bin(1))
    seed.append(bin(1))
    seed.append(bin(0))
    if message=="attemptall":
        message = input("Enter message to decrypt : ")
        for trial in range(0,taps):
            cipher = pcryt_encryption.encrypt(message, seed, trial)
            print("For tap=", trial," output=",cipher)
    else:
        cipher = pcryt_encryption.encrypt(message, seed, taps)
        return print(cipher)

main()
    
