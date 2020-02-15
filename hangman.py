
import random

line = ['rainbow', 'computer', 'science', 'programming',  
         'python', 'mathematics', 'player', 'condition',  
         'reverse', 'water', 'board', 'imam', 'samiul', 
         'noor', 'google', 'daffodil', 'dhaka', 'ahasan'] 
loadWords = random.choice(line)

def wordGuessed(secretWord, lettersGuessed):
    count=0
    for letters in secretWord:
        if letters in lettersGuessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False
    

def getWord_Guess(secretWord, letterGuess):
    string = ""
    
    for key in secretWord:
        if key in letterGuess:
            string += key
            
        else:
            string += "_"
        
    return string


def getAvailabeleLetters(letterGuess):
    string = ""
    count = 0
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in s:
        if letter in letterGuess:
            count += 1
            
        else:
            string += letter
            
    return string


def hangman(secretWord):
    length = len(secretWord)
    
    print("I'm thinking", length, "letter long word.")
    chances = 2 * len(secretWord)
    
    letterGuess = []
    
    while (chances != 0):
        
        if secretWord != getWord_Guess(secretWord, letterGuess):
            print("\n\tYou have", chances, "guesses left")
            
            guess = input("Please guess a letter: ")
            guessLowerCase = guess.lower()
            
            if guessLowerCase in letterGuess:
                print("You Have already guessed that letter: ", getWord_Guess(secretWord, letterGuess))
                
            elif guessLowerCase not in secretWord:
                print("That letter is not in my word: ", getWord_Guess(secretWord, letterGuess))
                chances -= 1
                
            else:
                letterGuess.append(guessLowerCase)
                print("Good Guess: ", getWord_Guess(secretWord, letterGuess))
                
            letterGuess.append(guessLowerCase)
            
        elif secretWord == getWord_Guess(secretWord, letterGuess):
            print("Congratulations, You Win!")
            break
        
    else:
        print("Sorry, You ran out. The word was \'" + secretWord + "\'.")
        
secretWord = loadWords
hangman(secretWord)
            
    
