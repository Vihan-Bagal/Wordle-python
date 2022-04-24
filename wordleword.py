#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from fancyword import FancyWord

class WordleWord(FancyWord):
    
    # setCorrect, setMisplaced,and setNotUsed are defined below. They are used to set letters to certain colors based on their correctness
    def setCorrect(self, pos):
        self.setColorAt(pos, "green")

    def setMisplaced(self, pos):
        self.setColorAt(pos, "yellow")

    def setNotUsed(self, pos):
        self.setColorAt(pos, "grey")

    def isCorrect(self, pos):
        return ("green" == self.colorAt(pos))
    # If the letter is in the correct position then it will turn green
    def isMisplaced(self, pos):
        return ("yellow" == self.colorAt(pos))
    # If the letter is in the correct word but not in the correct position, it will turn yellow
        
    def isNotUsed(self, pos):
        return ("grey" == self.colorAt(pos))
    # If the letter is not in the correct word, it turns grey