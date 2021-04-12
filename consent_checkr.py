# Consent Checker v0.8


while True:
    print("Welcome to Consent Checkr v0.7!")
    print("*******************************")


    your_age = int(input("Enter  your age: "))
    other_age = int(input("Enter other person's age: "))

    if (your_age == 18 and other_age == 15):
        print("\n********************")
        print("\nNot this time Carson")
        print("\n********************")


    elif (your_age < 18 or other_age < 18):
        print("ACHTUNG\n**NONCE DETECTED**\nINFO PASSED ONTO RELEVENT AUTHORITIES\n*******************************")



    elif (your_age > other_age):
        min_age = (your_age/2)+7

        if (other_age >= min_age):
            print("You're good to go!\n*******************************")

        if (other_age < min_age):
            print("**You're in the danger zone**\n*******************************")



    elif (other_age > your_age):
        min_age = (other_age/2)+7

        if (your_age >= min_age):
            print("You're good to go!\n*******************************")

        if (your_age < min_age):
            print("**You're in the danger zone**\n*******************************")

    try_again = input("\n\nTry again?  (Press Enter else n to quit)\n")
    if (try_again.lower() == 'n'):
            break 

input("\nPress Enter to exit")
