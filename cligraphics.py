from turtle import color
import game
import curses
from curses import wrapper
from wordleword import WordleWord
import time
from wordbank import WordBank
from wordleplayer import WordlePlayer

#Creates the player
player = WordlePlayer("Player", 6)

stdscr = curses.initscr()

curses.curs_set(0)

#INITALIZE ALL THE COLORS  
curses.start_color()

curses.init_color(curses.COLOR_YELLOW, 800, 800, 0)
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)


title = "WORDLE"


def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return i
    return False

def markGuess(word, guess, alphabet, alphabetColor):
    wordCopy = word
    colorList = [None, None, None, None, None]


    for i in range(len(guess)):

        if(type(search(alphabet[0], guess[i])) == int):
            idx1 = 0
            idx2 = search(alphabet[0], guess[i])
        elif(type(search(alphabet[1], guess[i])) == int):
            idx1 = 1
            idx2 = search(alphabet[1], guess[i])
        else:
            idx1 = 2
            idx2 = search(alphabet[2], guess[i])

        if(wordCopy[i] == guess[i]):
            colorList[i] = curses.color_pair(1)
            alphabetColor[idx1][idx2] = curses.color_pair(1)

            wordCopy = wordCopy[:i] + "#" + wordCopy[i+1:]


        elif(guess[i] in wordCopy):
            colorList[i] = curses.color_pair(2)
            alphabetColor[idx1][idx2] = curses.color_pair(2)

            index = wordCopy.index(guess[i])

            wordCopy = wordCopy[:index] + "#" + wordCopy[index+1:]


        else:
            colorList[i] = curses.color_pair(3)
            alphabetColor[idx1][idx2] = curses.color_pair(3)


    return colorList

def IsValid(guess, all_words):

    #print(all_words.contains(guessWord.word))
    if(len(guess) != 5):
        return False
    if(not all_words.contains("".join(guess))):
        return False

    return True


def draw(stdscr, letters, colors, alpha, alphaColor):
    stdscr.clear()

    centerX = int((curses.COLS - 29) / 2)
    centerY = int((curses.LINES - 24) / 2) - 5


    stdscr.addstr(0, int(curses.COLS/2) -  int(len(title)/2), title)
    for i in range(6):
        
        for x in range(5):

            stdscr.addstr(i * 3 + centerY, (x * 6) + centerX, "┌───┐", colors[i][x])
            stdscr.addstr(i * 3 + 1 + centerY, (x * 6) + centerX, "│ ", colors[i][x])
            stdscr.addstr(i * 3 + 1 + centerY, (x * 6 + 2) + centerX, letters[i][x].upper(), colors[i][x])
            stdscr.addstr(i * 3 + 1 + centerY, (x * 6 + 3) + centerX, " │", colors[i][x])
            stdscr.addstr(i * 3 + 2 + centerY, (x * 6) + centerX, "└───┘", colors[i][x])


    center = (curses.COLS-60) // 2
    alphaDown = int(curses.LINES / 1.8 )

    for i in range(3):
        
        for x in range(10-i):

            stdscr.addstr(i * 3 + alphaDown, 3*i + (x * 6) + center , "┌───┐", alphaColor[i][x])
            stdscr.addstr(i * 3 + 1 + alphaDown, 3*i + (x * 6) + center , "│ ", alphaColor[i][x])
            stdscr.addstr(i * 3 + 1 + alphaDown, 3*i + (x * 6 + 2)+ center  , alpha[i][x].upper(), alphaColor[i][x])
            stdscr.addstr(i * 3 + 1 + alphaDown, 3*i + (x * 6 + 3) + center , " │", alphaColor[i][x])
            stdscr.addstr(i * 3 + 2 + alphaDown, 3*i + (x * 6) + center , "└───┘", alphaColor[i][x])



def LoseScreen(stdscr, answer, tries):
    stdscr.clear()
    stdscr.addstr(int(curses.LINES/2) - 5, (curses.COLS - len("you lose"))//2, "YOU LOSE")
    stdscr.addstr(int(curses.LINES/2) -3, int(curses.COLS - 21)//2, "CORRECT ANSWER: " + answer)
    stdscr.addstr((curses.LINES//2) + -1, (curses.COLS - len("(Press SPACE to Play Again or ENTER to Quit)"))//2, "(Press SPACE to Play Again or ENTER to Quit)")
    player.updateStats(False, tries)
    counter = 1
    for i in player.displayStatsCLI():
        stdscr.addstr((curses.LINES//2) + counter, (curses.COLS - 10)//2, i)
        counter += 1

    key = (stdscr.getch())

    if(key == ord(" ")):
        return False   
    if(key == 10):
        return True 

def WinScreen(stdscr, tries):
    stdscr.clear()
    stdscr.addstr((curses.LINES//2), (curses.COLS - len("YOU WIN"))//2, "YOU WIN")
    stdscr.addstr((curses.LINES//2) + 1, (curses.COLS - len("(Press SPACE to Play Again or ENTER to Quit)"))//2, "(Press SPACE to Play Again or ENTER to Quit)")

    player.updateStats(True, tries)
    counter = 5
    for i in player.displayStatsCLI():
        stdscr.addstr((curses.LINES//2) + counter, (curses.COLS - len(i))//2, i)
        counter += 1
    key = (stdscr.getch())

    if(key == ord(" ")):
        return False   
    if(key == 10):
        return True 


def main(stdscr):

    currentLine = 0
    currentChar = 0
    wordArray = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
    d = curses.color_pair(4)
    colorArray = [[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]]

    alphabet = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"], ["z", "x", "c", "v" ,"b", "n", "m", ","]]
    alphabetColor = [[d, d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d]]

    draw(stdscr, wordArray, colorArray, alphabet, alphabetColor)

    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")

    answer = words.getRandom()


    while True:
        #freezes the program until a key is pressed. The key is then saved
        key = stdscr.getch()

        #If the enter key is pressed
        if(key == 10):

            #if it is a valid guess, mark it, otherwise delete it
            if(IsValid("".join(wordArray[currentLine]), all_words)):
                colorArray[currentLine] = markGuess(answer, wordArray[currentLine], alphabet, alphabetColor)
                win = True
                for i in colorArray[currentLine]:
                    if(i != 256):
                        win = False
                if(win):
                    if(WinScreen(stdscr, currentLine)):
                        quit()
                    else:
                        currentLine = -1
                        currentChar = 0
                        wordArray = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
                        colorArray = [[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]]
                        alphabet = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"], ["z", "x", "c", "v" ,"b", "n", "m", ","]]
                        alphabetColor = [[d, d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d]]
                        answer = words.getRandom()
                        draw(stdscr, wordArray, colorArray, alphabet, alphabetColor)

            else:
                wordArray[currentLine] = [" "," "," "," "," "]
                currentLine -= 1

            if(currentLine == 5):
                if(LoseScreen(stdscr, answer, currentLine)):
                    quit()
                else:
                    currentLine = -1
                    currentChar = 0
                    wordArray = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
                    colorArray = [[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]]
                    alphabet = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"], ["z", "x", "c", "v" ,"b", "n", "m", ","]]
                    alphabetColor = [[d, d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d, d], [d, d, d, d, d, d, d, d]]
                    answer = words.getRandom()
                    draw(stdscr, wordArray, colorArray, alphabet, alphabetColor)   
                

            currentLine += 1
            currentChar = 0

        #If the backspace key is pressed
        elif(key == 127):
            wordArray[currentLine][currentChar-1] = " "
            currentChar -= 1
            if(currentChar < 0):
                currentChar = 0

        #checks if you finished typing a word
        elif(currentChar == 5):
            pass
        #If a character key is pressed
        elif(chr(key) in "qwertyuiopasdfghjklzxcvbnm"):
            wordArray[currentLine][currentChar] = chr(key)
            currentChar += 1

        draw(stdscr, wordArray, colorArray, alphabet, alphabetColor)

        stdscr.refresh()
    stdscr.getkey()

wrapper(main)