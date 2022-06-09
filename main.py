# from rich import print
import time
import random
import pickle
from english_words import english_words_lower_alpha_set as ewords
import termplotlib as tpl

words = {
    # puzzle words
    # list adapted from https://7esl.com/4-letter-words/
    'AREA',
    'ARMY',
    'BABY',
    'BACK',
    'BALL',
    'BAND',
    'BANK',
    'BASE',
    'BILL',
    'BODY',
    'BOOK',
    'CALL',
    'CARD',
    'CARE',
    'CASE',
    'CASH',
    'CITY',
    'CLUB',
    'COST',
    'DATE',
    'DEAL',
    'DOOR',
    'DUTY',
    'EAST',
    'EDGE',
    'FACE',
    'FACT',
    'FARM',
    'FEAR',
    'FILE',
    'FILM',
    'FIRE',
    'FIRM',
    'FISH',
    'FOOD',
    'FOOT',
    'FORM',
    'FUND',
    'GAME',
    'GIRL',
    'GOAL',
    'GOLD',
    'HAIR',
    'HALF',
    'HALL',
    'HAND',
    'HEAD',
    'HELP',
    'HILL',
    'HOME',
    'HOPE',
    'HOUR',
    'JACK',
    'KIND',
    'KING',
    'LACK',
    'LADY',
    'LAND',
    'LIFE',
    'LINE',
    'LIST',
    'LOOK',
    'LORD',
    'LOSS',
    'LOVE',
    'MARK',
    'MIND',
    'MISS',
    'MOVE',
    'NAME',
    'NAME',
    'NEED',
    'NEWS',
    'NOTE',
    'PAGE',
    'PAIN',
    'PAIR',
    'PARK',
    'PART',
    'PAST',
    'PATH',
    'PLAN',
    'PLAY',
    'POST',
    'RACE',
    'RAIN',
    'RATE',
    'REST',
    'RISE',
    'RISK',
    'ROAD',
    'ROCK',
    'ROLE',
    'ROOM',
    'RULE',
    'SALE',
    'SEAT',
    'SHOP',
    'SHOW',
    'SIDE',
    'SIGN',
    'SITE',
    'SIZE',
    'SKIN',
    'SORT',
    'STAR',
    'STEP',
    'TASK',
    'TUSK',
    'TEAM',
    'TERM',
    'TEST',
    'TEXT',
    'TIME',
    'TOUR',
    'TOWN',
    'TREE',
    'TURN',
    'TYPE',
    'UNIT',
    'USER',
    'VIEW',
    'WALL',
    'WEEK',
    'WEST',
    'WILL',
    'WIND',
    'WINE',
    'WOOD',
    'WORK',
    'YEAR',
    'BEAR',
    'BEAT',
    'BLOW',
    'BURN',
    'CAST',
    'COME',
    'COOK',
    'COPE',
    'DARE',
    'DENY',
    'DRAW',
    'DROP',
    'EARN',
    'FAIL',
    'FALL',
    'FEAR',
    'FEEL',
    'FILL',
    'FIND',
    'GAIN',
    'GIVE',
    'GROW',
    'HANG',
    'HATE',
    'HAVE',
    'HEAD',
    'HEAR',
    'HIDE',
    'HOLD',
    'HOPE',
    'HURT',
    'JOIN',
    'JUMP',
    'KEEP',
    'KILL',
    'KNOW',
    'LAST',
    'LEAD',
    'LEND',
    'LIFT',
    'LIKE',
    'LINK',
    'LIVE',
    'LOSE',
    'LOVE',
    'MAKE',
    'MEET',
    'MIND',
    'MOVE',
    'MUST',
    'NOTE',
    'OPEN',
    'PASS',
    'PICK',
    'PLAN',
    'PLAY',
    'PULL',
    'PUSH',
    'READ',
    'RELY',
    'REST',
    'RIDE',
    'RING',
    'RISE',
    'ROLL',
    'RULE',
    'SAVE',
    'SEEK',
    'SEEM',
    'SELL',
    'SEND',
    'SHED',
    'SHOW',
    'SHUT',
    'SING',
    'SLIP',
    'STAY',
    'STOP',
    'SUIT',
    'TAKE',
    'TALK',
    'TELL',
    'TEND',
    'TEST',
    'TURN',
    'VARY',
    'VIEW',
    'VOTE',
    'WAIT',
    'WAKE',
    'WALK',
    'WANT',
    'WARN',
    'WASH',
    'WEAR',
    'WISH',
    'WORK',
    'ABLE',
    'BACK',
    'BARE',
    'BASS',
    'BLUE',
    'BOLD',
    'BUSY',
    'CALM',
    'COLD',
    'COOL',
    'DAMP',
    'DARK',
    'DEAD',
    'DEAF',
    'DEAR',
    'DEEP',
    'DUAL',
    'DULL',
    'EASY',
    'EVIL',
    'FAIR',
    'FAST',
    'FINE',
    'FIRM',
    'FLAT',
    'FOND',
    'FOUL',
    'FREE',
    'FULL',
    'GLAD',
    'GOOD',
    'GREY',
    'GRIM',
    'HARD',
    'HIGH',
    'HOLY',
    'HUGE',
    'JUST',
    'KEEN',
    'LATE',
    'LAZY',
    'LIKE',
    'LIVE',
    'LONE',
    'LONG',
    'LOUD',
    'MAIN',
    'MALE',
    'MASS',
    'MEAN',
    'MERE',
    'MILD',
    'NEAR',
    'NEAT',
    'NEXT',
    'NICE',
    'OKAY',
    'ONLY',
    'OPEN',
    'PALE',
    'PAST',
    'PINK',
    'POOR',
    'PURE',
    'RARE',
    'REAL',
    'REAR',
    'RICH',
    'RUDE',
    'SAFE',
    'SAME',
    'SICK',
    'SLIM',
    'SLOW',
    'SOFT',
    'SOLE',
    'SORE',
    'SURE',
    'TALL',
    'THEN',
    'THIN',
    'TIDY',
    'TINY',
    'TRUE',
    'VAIN',
    'VAST',
    'VERY',
    'VICE',
    'WARM',
    'WEAK',
    'WIDE',
    'WILD',
    'WISE',
    'ZERO'

}
colors = {
    # ansi color escape codes
    'black': '\u001b[30m',
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m',
    'none': '\u001b[0m'
}


def flush_input(): # Code from https://stackoverflow.com/questions/2520893/how-to-flush-the-input-stream
    #stops players from typing during printing
    try:
        import msvcrt
        print('msvcrt')
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

class Letter: #represents a character
    def __init__(self, name, pos, color='none'):
        self.name = name
        self.pos = pos
        self.color = color

    def changeColor(self, newColor):
        self.color = newColor

    def typeOut(self): # returns the name sandwiched in color codes
        return colors[self.color] + self.name + colors['none']

class SaveFile: # object that gets pickled
    def __init__(self, played, wins, curr_streak, max_streak, distribution):
        self.played = played
        self.wins = wins
        self.curr_streak = curr_streak
        self.max_streak = max_streak
        self.distribution = distribution

# def addColor(s, color): #Unused
#     return colors[color] + s + colors['none']

def printSpaced(inList): #for printing the board
    for i in inList:
        print(i)

def dramaticPrint(inList): # for printing the word dramatically
    for i in inList:
        time.sleep(0.5)
        print(i.typeOut(), end=' ')
    time.sleep(2)
    print()

def main():
    while True: #setup code, runs before game
        toGuess = random.choice(list(words))
        unfinished = True
        tries = 5
        theBoard = []
        tryNum = 0
        for c in range(tries): #make blank spaces, scales with tries
            theBoard.append('|- - - -|')
        while unfinished: #runs until solved or out of tries
            if tryNum != tries:# try counter
                tryNum += 1
                letterCheck = True
                while letterCheck: #asks for input and checks for validity
                    guessedStr = input('>>')
                    isLetters = True
                    appearances = dict()
                    for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        appearances[a] = toGuess.count(a)
                    letterList = []
                    finalList = [None, None, None, None]
                    if len(guessedStr) == 4:
                        for strNum in range(len(guessedStr)):
                            if not guessedStr[strNum].capitalize().isalpha():
                                isLetters = False
                            letterToCreate = Letter(guessedStr[strNum].capitalize(), strNum)
                            letterList.append(letterToCreate)
                        for l1 in letterList:
                            letterToColor = l1
                            if letterToColor.name == toGuess[letterToColor.pos]:
                                letterToColor.changeColor('green')
                                appearances[letterToColor.name] -= 1
                                finalList[letterToColor.pos] = letterToColor
                        for l2 in letterList:
                            letterToColor = l2
                            if not letterToColor.color == 'green':
                                if letterToColor.name in toGuess and appearances[letterToColor.name] > 0:
                                    letterToColor.changeColor('yellow')
                                    appearances[letterToColor.name] -= 1
                                    finalList[letterToColor.pos] = letterToColor
                                else:
                                    letterToColor.changeColor('none')
                                    finalList[letterToColor.pos] = letterToColor
                        if isLetters:
                            if guessedStr.upper() == toGuess or guessedStr.lower() in ewords:
                                letterCheck = False
                            else:
                                print('Try a four-letter word.')
                        else:
                            print('Try a four-letter word.')
                    else:
                        print('Try a four-letter word.')
                # letter1 = Letter(guessedStr[0].capitalize(), 1) # creates letters out of input
                # letter2 = Letter(guessedStr[1].capitalize(), 2)
                # letter3 = Letter(guessedStr[2].capitalize(), 3)
                # letter4 = Letter(guessedStr[3].capitalize(), 4)
                # finalList = [letter1, letter2, letter3, letter4]
                # for i in finalList: #colors letters based on puzzle word
                #     if i.name == toGuess[i.pos-1]:
                #         i.changeColor('green')
                #     elif i.name in toGuess:
                #         i.changeColor('yellow')
                #     else:
                #         i.changeColor('none')
                dramaticPrint(finalList) #big reveal
                print('|=+=+=+=|') #border for fanciness
                theBoard[tryNum-1] = f'|{finalList[0].typeOut()} {finalList[1].typeOut()} {finalList[2].typeOut()} {finalList[3].typeOut()}|'
                printSpaced(theBoard)
                print('|=+=+=+=|') #border for fanciness
                if f'{finalList[0].name}{finalList[1].name}{finalList[2].name}{finalList[3].name}' == toGuess: # win state
                    try: # if the save exists, read it in
                        with open('save.pkl', 'rb') as f:
                            save = pickle.load(f)
                    except: # if it doesn't, make a save
                        with open('save.pkl', 'wb') as f:
                            save = SaveFile(0, 0, 0, 0, [0, 0, 0, 0, 0])
                            pickle.dump(save, f)
                    #change save attributes
                    newPlayed = save.played+1
                    newWins = save.wins+1
                    newCurrStreak = save.curr_streak+1
                    if save.curr_streak+1 > save.max_streak:
                        newMax = save.curr_streak+1
                    else:
                        newMax = save.max_streak
                    newDist = save.distribution
                    newDist[tryNum-1] += 1
                    with open('save.pkl', 'wb') as f: #save the file
                        pickle.dump(SaveFile(newPlayed, newWins, newCurrStreak, newMax, newDist), f)
                    print(f'You won in {tryNum} guess(es)!')
                    time.sleep(3)
                    print('---Stats---')
                    print(f'Played: {newPlayed}, Win %: {round((newWins / newPlayed) * 100, 2)},')
                    print(f'Current Streak: {newCurrStreak}, Max Streak: {newMax}')
                    print('---Guess Distribution---')
                    fig = tpl.figure() # bar graph
                    fig.barh(newDist, ["1", "2", "3", "4", "5"], force_ascii=True)
                    fig.show()
                    another = input('Play another? [Y/N] : ') # asks if you wanna play again
                    if another == 'Y' or another == 'y':
                        print('Starting a new game...')
                        time.sleep(3)
                        unfinished = False
                    elif another == 'N' or another == 'n':
                        print('Okay, see you later, champ.')
                        exit()
                    else:
                        print("I don't know what that means so I'll take it as a yes.")
                        print('Starting a new game...')
                        time.sleep(3)
                        unfinished = False
            else:
                try:
                    with open('save.pkl', 'rb') as f:
                        save = pickle.load(f)
                except:
                    with open('save.pkl', 'wb') as f:
                        save = SaveFile(0, 0, 0, 0, [0, 0, 0, 0, 0])
                        pickle.dump(save, f)
                newPlayed = save.played+1
                newWins = save.wins
                newCurrStreak = 0
                newMax = save.max_streak
                newDist = save.distribution
                with open('save.pkl', 'wb') as f:
                    pickle.dump(SaveFile(newPlayed, newWins, newCurrStreak, newMax, newDist), f)
                print(f"You're out of guesses! The word was {toGuess}.")
                time.sleep(3)
                print('---Stats---')
                print(f'Played: {newPlayed}, Win %: {round((newWins / newPlayed) * 100, 2)},')
                print(f'Current Streak: {newCurrStreak}, Max Streak: {newMax}')
                print('---Guess Distribution---')
                fig = tpl.figure()
                fig.barh(newDist, ["1", "2", "3", "4", "5"], force_ascii=True)
                fig.show()
                another = input('Play another? [Y/N] : ')
                if another == 'Y' or another == 'y':
                    print('Starting a new game...')
                    time.sleep(3)
                    unfinished = False
                elif another == 'N' or another == 'n':
                    print('Okay, quitter.')
                    exit()
                else:
                    print("I don't know what that means so I'll take it as a yes.")
                    print('Starting a new game...')
                    time.sleep(3)
                    unfinished = False

def test():
    while True:
        flush_input()
        time.sleep(1)
        input('test')

if __name__ == '__main__':
    main()