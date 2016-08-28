nice = 0
mean = 0

def main():
    start()

def start():
    print "Hello and welcome to nice or mean!"
    name = raw_input ("What's your name? : ")
    print "Hi and welcome, "+name+"!"
    print "In this game, you will be greeted by several people.  You can be nice or mean to them."
    print "At the end of the game your fate will be determined by the way you acted."

    choice = raw_input("Do you want to play?  y/n ")

    if choice == "y":
        print "Great!  Use 'm' for mean and 'n' for nice!"
        begin()
        
    if choice == "n":
        print "Ok, bye..."

def begin():
    global nice
    global mean

    if nice > 2:
            print "You are very nice!  You WIN $1,000,000!!"
            choice = raw_input("Do you want to play again? y/n ")
            
            if choice == "y":
                 print "Okay lets go!"
                 nice = 0
                 begin ()

            if choice == "n":
                print "See ya nice person!"
                exit()

    if mean > 2:
            print "You are very mean!  You won the book titled 'How to be nice for Dummies'"
            choice = raw_input("Do you want to play again? y/n ")

            if choice == "y":
                print "Okay, maybe be nicer this time."
                mean = 0
                begin()
                
            if choice == "n":
                print "God Bless and remember the golden rule!"
                exit()

            elif choice != "y"+"n":
                print "Please enter y or n"

                if choice == "y":
                    begin()
                    
                if choice == "n":
                    print "Adios!"
                    exit()

                if choice != "y" + "n":
                    choice = raw_input ("Quit messin' around!  Do you want to play? y/n ")

    pick = raw_input("Someone wants to talk to you.  Will you be nice or mean? n/m " )
            
    if pick == "n":
            print "They have smiled and waved bye."
            nice = nice + 1
            print "You currently have " +str(nice) + " nices."
            begin()

    if pick == "m":
            print "They flipped you off and frowned!"
            mean = mean + 1
            print "You currently have " +str(mean)+  " means."
            begin()

start()
                      
