# a password generator
#good password would consist of special characters, number, capital and small letters

import string
import random

def main():
    type = raw_input("Select the complexity of your password \n 1) Simple \n 2) Medium \n 3) Complex \n 4) Unbeatable \n 5) Other\n >")

    if (type == "1"):
        passwd = createSimplePwd()

    elif (type == "2"):
        passwd = createPwd(5, 5)

    elif (type == "3"):
        passwd = createPwd(9, 7)

    elif type == "4":
        passwd = createPwd(15, 5)

    elif type == "5":
        letters = raw_input ("How many letters would you like in your pasword: >")
        spChar = raw_input ("How many special characters would you like in your pasword: >")
        passwd = createPwd(int(letters), int(spChar))

    else:
        print "Invalid Input"


    print "Your password is : ", passwd

def randChars(n):
    return ''.join(random.choice(string.letters) for x in range(n))
	
	
def randSpecialChar():
    choic = random.choice("!%#*^`~?)(")
    return choic

def createPwd(c, s):
    num = random.randint(0,999)
    char = []
    letters1 = randChars(c)
    letters2 = randChars(c)
	
    for i in range(0,s):
        char.append(randSpecialChar())
    passwdAr = [num, letters1, letters2]
    passwdNew = passwdAr + char
    random.shuffle(passwdNew)
    passwd = ''.join(map(str, passwdNew))	
    return passwd
	
def createSimplePwd():
    num = random.randint(100,999)
    words = ["sunshine","barbie", "crystal","sharp","plank","sugary","forward","epitome","success","darth","autumn","playlist",
    "superman","extreme","digital","bananas", "orange","rugby","teacher","slave","singsong","unicorn","parkour","happiness", 
	"cheeky","tulip","laser","enemy","break","berry","match","award","exile","rough","scene","trunk","habit","black","babel","wodgy"
	"alowe","karat","barmy","lulie"]
    random.shuffle(words)
    return words[random.randint(0,len(words)-1)]+randSpecialChar()+str(num)

if __name__ == "__main__":
    main()
