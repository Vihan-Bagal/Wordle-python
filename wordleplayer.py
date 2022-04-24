#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreakVal() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from player import Player

    # Many of these functions are self explanatory 
class WordlePlayer:
    def __init__(self, name, maxTries):
        self.name = name
        self.lossAmt = 0
        self.winAmt = 0
        self.maxStreakVal = 0
        self.currentStreakVar = 0
        self.guessStreak = [0,0,0,0,0,0]
    
    def winPercentage(self):
        totalGames = self.gamesPlayed()
        winRate = self.winAmt/totalGames
        return(winRate*100)

    def gamesPlayed(self):
        gamesPlayed = self.lossAmt + self.winAmt
        return(gamesPlayed)
    
    def currentStreak(self):
        return(self.currentStreakVar)

    def maxStreak(self):
        return(self.maxStreakVal)

    # Gets the stats and prints them out in a certain format
    def displayStats(self):
        total = (int(self.winAmt) + int(self.lossAmt))
        print("Games Played: {}".format(total))
        if(self.lossAmt != 0):
            print("Win %:{}".format((self.winPercentage() * 100)))
        else:
            print("Win %: 100")
        print("Current Streak: {}".format(self.currentStreakVar))
        print("Max Streak: {}".format(self.maxStreakVal))
        print("Guess Distribution")

        counter = 0
        for g in self.guessStreak:
            '''printStr = ("#" * (10 * g) + "#")
            newStr = printStr[:21]'''
            if(g == 0):
                newStr = "#"
            else:
                newStr = "#" * 21

            print(str(counter + 1)+ " : " + newStr + " " + str(g))
            counter += 1

    # Display stats for the CLI
    def displayStatsCLI(self):

        returnStr = []

        total = (int(self.winAmt) + int(self.lossAmt))
        returnStr.append("Games Played: {}".format(total))
        if(self.lossAmt != 0):
            returnStr.append("Win %:{}".format((self.winPercentage() * 100)))
        else:
            returnStr.append("Win %: 100")
        returnStr.append("Current Streak: {}".format(self.currentStreakVar))
        returnStr.append("Max Streak: {}".format(self.maxStreakVal))
        returnStr.append("Guess Distribution")

        counter = 0
        for g in self.guessStreak:
            if(g == 0):
                newStr = "#"
            else:
                newStr = "#" * 21

            returnStr.append(str(counter + 1)+ " : " + newStr + " " + str(g))
            counter += 1
        return returnStr

    def updateStats(self, won, tries):
        tries -= 1

        if (won):
            self.currentStreakVar += 1
            self.winAmt += 1
            self.guessStreak[tries] += 1
            tries = 0
        else:
            self.currentStreakVar = 0
            self.lossAmt += 1

        if(self.currentStreakVar > self.maxStreakVal):
            self.maxStreakVal = self.currentStreakVar

