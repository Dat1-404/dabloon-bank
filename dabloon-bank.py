import pickle
import os

#Reset amounts
depositamount = int(0)
withdrawalamount = int(0)

print("Hello, and welcome to the Dabloon Bank, the most trusted bank for dabloons!")
var1 = int(input("What would you like to do?\n1. About us\n2. Deposit\n3. Withdraw\n4. Check balance\n5. Create account (Start with this if you haven't already.)\n6. How to delete the program.\n"))

if var1 == 1 :
    print("We were founded by TikTok user @dat1___ on November 21, 2022."),
    print("We were founded to help protect you from dabloon thieves!"),
    print("Have fun collecting dabloons, and we're happy you're here!"),
    input("")

if var1 == 5 : 
    var2 = input("Using this will create an account if you haven't already or reset it. Are you sure you want to do this? (y/n)")
    if var2 == "yes" or var2 == "y" :
        dabloons = 0
        pickle.dump(dabloons, open("dabloons.dat", "wb"))
        ph = input("Dabloons successfully saved. You may now perform actions with it.")
        exit()
    if var2 == "no" or var2 == "n" :
        exit()

if var1 == 2 :
    dabloons = pickle.load(open("dabloons.dat", "rb"))
    depositamount = int(input("Enter the amount of dabloons you want to deposit: "))
    dabloons = dabloons + depositamount
    pickle.dump(dabloons, open("dabloons.dat", "wb"))
    ph = input("Successfully deposited "+str(depositamount)+" dabloons.")

if var1 == 3 :
    dabloons = pickle.load(open("dabloons.dat", "rb"))
    withdrawalamount = int(input("Enter the amount of dabloons you want to withdraw: "))
    dabloons = dabloons - withdrawalamount
    pickle.dump(dabloons, open("dabloons.dat", "wb"))
    ph = input("Successfully withdrawed "+str(withdrawalamount)+" dabloons.")

if var1 == 4 :
    dabloons = pickle.load(open("dabloons.dat", "rb"))
    ph = input("You have "+str(dabloons)+" dabloons.")

if var1 == 6 : 
    print("To delete the program entirely, delete the folder that contains this file. If you removed this program from the folder, look up dabloons.dat, and delete it (that's where data is stored).")
    input("Once it has been deleted, or it isn't there, delete this file as well. We're sad to see you go. Good luck traveler!")
    
