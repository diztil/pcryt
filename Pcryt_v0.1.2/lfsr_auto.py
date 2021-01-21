# Client for LFSR encryption "Pcryt" modules
# @author dmimukto 2021

# MODULE IMPORTS
import sys
import pcryt_encryption
import os.path

# MAIN PROGRAM
def main():
    seed = sys.argv[1]
    taps = int(sys.argv[2])
    seed_list = []
    for index in range(len(seed)):
        seed_list.append(bin(int(seed[index])))
    inputfilename = "pcryt_input.txt"
    outputfilename = "pcryt_output.txt"
    print("File To Encrypt :", inputfilename)
    print("File For Output :", outputfilename)
    if os.path.isfile(inputfilename):
        fileIn = open(inputfilename, "r")
        fileIn.seek(0)
        firstline = fileIn.readline()
        print("\nThe first line (preview):",firstline)
        fileIn.seek(0)
        all_lines = fileIn.readlines()
        print("There are",len(all_lines),"lines in the text file.")
        fileIn.seek(0)
        fileOut = open(outputfilename, "w")
        fileOut.seek(0)
        for line in range(len(all_lines)):
            message = fileIn.readline()
            encrypted_line = pcryt_encryption.encrypt(message,seed_list,taps)
            fileOut.write(encrypted_line+chr(10))
        fileOut.close()
        print("\nEncryption complete :", inputfilename, "to", outputfilename)
    else:
        print("\nInput file not found.")
        

main()
    
