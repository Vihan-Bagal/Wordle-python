import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from player import Player


# Vihan Bagal and Siddharth Gupta
# Snapshot 1 - Finished both classes and started on mark guess

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======

# Check each letter in the guessed word and compares to correct word, will mark using colors depending on correctness
def markGuess(word, guess, alphabet):
    wordCopy = word
    for i in range(5):

        if(wordCopy[i] == guess.word[i]):
            guess.setCorrect(i)

            alphabet.setCorrect(alphabet.word.index(guess.word[i]))
            wordCopy = wordCopy[:i] + "#" + wordCopy[i+1:]


        elif(guess.word[i] in wordCopy):
            guess.setMisplaced(i)
            index = wordCopy.index(guess.word[i])

            alphabet.setMisplaced(alphabet.word.index(guess.word[i]))
            wordCopy = wordCopy[:index] + "#" + wordCopy[index+1:]

        
        

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======


#Checks if a wordleWord is a valid guess
def IsValid(guess, all_words):
    guess.word = guess.word.lower()

    #print(all_words.contains(guessWord.word))
    if(len(guess.word) != 5):
        return False
    if(not all_words.contains(guess.word)):
        return False

    return True
    
    
# Initiates a round of Wordle
def playRound(players, words, all_words, settings):

    alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")
    answer = words.getRandom()
    answer = "lanes"
    tries = 0
    
    #n = input("Please enter your name: ")
    print("\nWelcome, let's play a game of wordle")

    for i in range(6):

        #Checks for Valid guesses: Repeats until a valid guess is given
        while True:
            guessWord = WordleWord(input("\nEnter your guess: "))
            if(IsValid(guessWord, all_words)):
                break
            else:
                print("\nPlease enter a valid word!")


        markGuess(answer, guessWord, alpha)
        print()
        print(guessWord)
        print(alpha)
        print()
        tries += 1
        
        if(guessWord.word == answer):
            print("\nCongradulations!, you guessed the correct word")
            players.updateStats(True, tries)
            players.displayStats()
            return
        


    print("The right answer was: " + answer)


    players.updateStats(False, tries)
    players.displayStats()
    



# Initiates a game of Wordle 
def playWordle():
    print("Let's play the game of Wordle!")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player
    play = WordlePlayer("george", 6)

    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")

    # start playing rounds of Wordle
    
    
    playRound(play, words, all_words, settings)

    while('y' in input("\nDo You Want To Play Again?: ").lower()):
        print()
        playRound(play, words, all_words, settings)

def main():
    playWordle()


if __name__ == "__main__":
    main()