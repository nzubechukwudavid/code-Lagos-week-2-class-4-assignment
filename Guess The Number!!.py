import time

import random
play_again = input("Would you like to play??")
while play_again == "yes":
        
    true = (random.randint(0,100))

    guess = int(input("Guess a number! \nIts between 0 and 100:\n"))

    
    if guess <= 100 and guess >= 0:
        
        while guess != true:
            if (abs(guess-true)) <= 5:                                                      #The absolute value function is the
                print("Your'e really, really close. ")                                   #workaround for the upper and lower limits i used in the
                guess = int(input("Come on!! Try another:\n"))               #previous code. this is a better way to avoid errors.
                                                                                                   #Also, i used the sleep function to delay the end of the program 
            elif (abs(guess-true)) <= 10:                                            #Ill try to do a rock, paper ,scissors simulator next.
                                                                                               #Thank You.
                print("Your'e really close.")
                guess = int(input("Come on!! Try another:\n"))

            elif (abs(guess-true)) <= 20:
                print("Not too far off")
                guess = int(input("Come on!! Try another:\n"))

            elif (abs(guess-true)) <= 40:
                print("Your'e well off the mark!!")
                guess = int(input("Come on!! Try another:\n"))

            elif (abs(guess-true)) <= 70:
                print("Not. Even. Close.")
                guess = int(input("Come on!! Try another:\n"))

            else:
                print("You..... must have some sort of problem.")
                guess = int(input("Come on!! Try another:\n"))
        
    else:
        print("Hey, its a a guess between 1 and hundred, Genius")
        guess = int(input("Lets try that again:\n:"))
    print("Yay!! You got the number!")        
    play_again = input("Play again??     (yes/no)")

print("Come back later for more awesome games!!")
print("See ya!")
time.sleep(4)
