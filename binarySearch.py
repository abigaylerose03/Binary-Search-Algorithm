#!usr/bin/python 3


"""

This is a simple binary search alogrithm where the computer guesses
the user's secret number.
- ARP

"""


def y_or_n(prompt, yes_values={"y", "yes"}, no_values={"n", "no"}):
    
    """ Prompt for a yes or no response;
    return True for yes or False for no
    """
    
    while True:                                 
        response = input(prompt).strip().lower()   # removes unnecessary characters from user input and uncapitalizes the string
        if response in yes_values:                  
            return True
        elif response in no_values:                 
            return False


def main():
    print("Guessing game!!\n"
          "I, the computer, will try and guess your secret number.\n"
          "Let's begin...")

    attempts = 0                        # number of attempts the computer tries to get your hidden number
    got_it = False                      # assumes that the computer hasn't guessed the number yet
    
    lo_r = int(input("Enter the lower limit for the range: "))
    hi_r = int(input("Enter the higher limit for the range: "))


    # this while loop doesn't stop until the user enters a low number that's literally lower than the high number
    while(lo_r > hi_r):    
        print("Error! You can't enter your first number higher than the second.\n"
              "Enter again.")

        lo_r = int(input("Enter the lower limit for the range: "))
        hi_r = int(input("Enter the higher limit for the range: "))


    # this while loop calculates the midrange of the 'lo_r' and the 'hi_r'
    # and stops when it gets the number it approximates is the user's hidden number
    while round(hi_r - lo_r) > 1:
        mid_range = round((lo_r + hi_r) / 2)
        response = y_or_n("Is your number greater than " + str(mid_range) + "? Enter (y/n): ")

        if response:
            lo_r = mid_range
            attempts += 1
        elif response == False:
            hi_r = mid_range - 1
            attempts += 1
        else:
            print("Please input a valid response!")

    # this while loop guesses the number until the computer wins or loses
    while got_it == False:
        response = y_or_n("Is your number " + str(lo_r) + "? ")
        if response:                                                # if the computer wins, output this sassy message
            print("I actually knew that all along. " + "Your number is " + str(lo_r) + ". " + "It took " + str(attempts) + " times!")
            got_it = True
        elif response == False:                                     # if the computer guesses wrong, increment low number by 1 until it exceeds the range                                    
            lo_r += 1
            attempts += 1
        else:
            print("Please enter a valid response.")

        if lo_r > round(hi_r + lo_r / 2):                           # this makes sure that the low number doesn't increment over the range set by the user.
                                                                    # If the computer still cant't guess the number, output this sad message
            print("Aww, I lost. I tried to guess your number in " + str(attempts) + " times.")
            got_it = True
            
        
                
if __name__== "__main__":
    main()         


        
    
