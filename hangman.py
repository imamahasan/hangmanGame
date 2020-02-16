
import random

admin_valu = ['rainbow', 'computer', 'science', 'programming',  
         'python', 'mathematics', 'player', 'condition',  
         'reverse', 'water', 'board', 'imam', 'samiul', 
         'noor', 'google', 'daffodil', 'dhaka', 'ahasan'] 
random_word = random.choice(admin_valu)
   

def guess_word(dynamicGuess, userGuess):
    string = ""
    
    for key in dynamicGuess:
        if key in userGuess:
            string += key
            
        else:
            string += "_"
        
    return string


def letters(userGuess):
    string = ""
    count = 0
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in s:
        if letter in userGuess:
            count += 1
            
        else:
            string += letter
            
    return string


def hangman(dynamicGuess):
    length = len(dynamicGuess)
    
    print("I'm thinking", length, "letter long word.")
    chances = 7
    valu = 0
    
    userGuess = []
    
    while (chances != 0):
        print("     ----------")
        print("     |        |")
        print("     |        " + ("O" if valu > 0 else ""))
        print("     |        " + ("/\\" if valu > 1 else ""))
        print("     |       " + ("/  \\" if valu > 2 else ""))
        print("     |        " + ("||" if valu > 3 else ""))      
        print("     |        " + ("/\\" if valu > 4 else ""))
        print("     |       " + ("/  \\" if valu > 5 else ""))
#        print("     |        " + ("->>" if valu > 6 else ""))
        print(" ----------")
        
        if dynamicGuess != guess_word(dynamicGuess, userGuess):
            print("\n\tYou have", chances, "chances")
            
            u_input = input("Please guess a letter: ")
            lowerCase = u_input.lower()
            
            if lowerCase in userGuess:
                print("Already guessed: ", guess_word(dynamicGuess, userGuess))
                
            elif lowerCase not in dynamicGuess:
                print("Letter is not in word: ", guess_word(dynamicGuess, userGuess))
                chances -= 1
                valu += 1
                
            else:
                userGuess.append(lowerCase)
                print("Good Guess: ", guess_word(dynamicGuess, userGuess))
                
            userGuess.append(lowerCase)
            
        elif dynamicGuess == guess_word(dynamicGuess, userGuess):
            print("Congratulations, You Win!")
            break
        
    else:
        print("Sorry, You ran out. The word was \'" + dynamicGuess + "\'.")
        
dynamicGuess = random_word
hangman(dynamicGuess)
