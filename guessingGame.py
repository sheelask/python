#program to guess the number given by user

def calcMid (start, end):
    return int(round(start+end)/2)    

#guess a number between 0 to 100
start = 0
end = 100
count = 1
print "Guess a number between 0 to 100"
raw_input("Press Enter to continue")
guess = calcMid(start,end)


while True:
    
    print 'Is this the number you guessed? - %d (Y/N)' %guess
    rv = raw_input()
    if (rv == 'N'):
        dist = raw_input("Is it lower than the guess or higher? (L/H)")
        if (dist == "L" or dist == 'l'):
            newGuess = calcMid(start, guess)
            end = guess  
            guess = newGuess
        elif ( dist == 'H' or dist == 'h'):
            newGuess = calcMid (end, guess)
            start = guess            
            guess = newGuess        
        count = count + 1
    elif (rv == 'Y'):
        print ("Superb! i guessed it right!")
        break
    else:
        print "Invalid input"
        continue
print "I guessed %d in %d attempts" %(guess, count)
