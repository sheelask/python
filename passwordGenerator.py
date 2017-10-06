# a password generator
#good password would consist of special characters, number, capital and small letters

import string
import random

def main():
    num = random.randint(0,100)
    letters1 = randChars(3)
    letters2 = randChars(5)
    char1 = randSpecialChar()
    char2 = randSpecialChar()
    passwdAr = [num, letters1, letters2, char1, char2]
    random.shuffle(passwdAr)
    passwd = ''.join(map(str, passwdAr))
    print "Your password is : ", passwd

def randChars(n):
    return ''.join(random.choice(string.letters) for x in range(n))
	
	
def randSpecialChar():
    return random.choice("!%#*^`~")

if __name__ == "__main__":
    main()
	
	
