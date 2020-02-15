
import random

word_file_name = "words.txt"


def loadWords():
#    print("Loading Word List From File.")
    
    in_file = open(word_file_name)
    line = in_file.readline()
    word_list = line.split()
    
    print(" ", len(word_list), "Words Loaded.")
#    print(word_list)
    
    return word_list


def chooseWord(word_list):   
    return random.choice(word_list)


word_list = loadWords()


def word_Guess(secretWord, letterGuess):
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
#        print("----------")
        
        if secretWord != word_Guess(secretWord, letterGuess):
            print("\n\tYou have", chances, "guesses left")
#            print("Available letters: ", getAvailabeleLetters(letterGuess))
            
            guess = input("Please guess a letter: ")
            guessLowerCase = guess.lower()
            
            if guessLowerCase in letterGuess:
                print("You Have already guessed that letter: ", word_Guess(secretWord, letterGuess))
                
            elif guessLowerCase not in secretWord:
                print("That letter is not in my word: ", word_Guess(secretWord, letterGuess))
                chances -= 1
                
            else:
                letterGuess.append(guessLowerCase)
                print("Good Guess: ", word_Guess(secretWord, letterGuess))
                
            letterGuess.append(guessLowerCase)
            
        elif secretWord == word_Guess(secretWord, letterGuess):
            print("Congratulations, You Win!")
            break
        
    else:
        print("----------")
        print("Sorry, You ran out. The word was \'" + secretWord + "\'.")
        
secretWord = "location"
hangman(secretWord)
            
    
    