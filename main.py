# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

words = {
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

class Letter:
    def __init__(self, name, pos, color='none'):
        self.name = name
        self.pos = pos
        self.color = color

    def changeColor(self, newColor):
        self.color = newColor

    def typeOut(self):
        return colors[self.color] + self.name + colors['none']

def addColor(s, color):
    return colors[color] + s + colors['none']

def printSpaced(inList):
    for i in inList:
        print(i)

def dramaticPrint(inList):
    for i in inList:
        time.sleep(0.5)
        print(i.typeOut(), end=' ')
    time.sleep(2)
    print()

def main():
    while True:
        toGuess = 'MAYO'
        unfinished = True
        tries = 5
        theBoard = []
        tryNum = 0
        for c in range(tries):
            theBoard.append('- - - -')
        while unfinished:
            if tryNum != tries:
                tryNum += 1
                letterCheck = True
                while letterCheck:
                    guessedStr = input('>>')
                    isLetter = True
                    for l in guessedStr:
                        if not l.isalpha():
                            isLetter = False
                    if isLetter and len(guessedStr) == 4:
                        letterCheck = False
                    else:
                        print('Try a four-letter word.')
                letter1 = Letter(guessedStr[0].capitalize(), 1)
                letter2 = Letter(guessedStr[1].capitalize(), 2)
                letter3 = Letter(guessedStr[2].capitalize(), 3)
                letter4 = Letter(guessedStr[3].capitalize(), 4)
                letterList = [letter1, letter2, letter3, letter4]
                for i in letterList:
                    if i.name == toGuess[i.pos-1]:
                        i.changeColor('green')
                    elif i.name in toGuess:
                        i.changeColor('yellow')
                    else:
                        i.changeColor('none')
                dramaticPrint(letterList)
                print('= = = =')
                theBoard[tryNum-1] = f'{letter1.typeOut()} {letter2.typeOut()} {letter3.typeOut()} {letter4.typeOut()}'
                printSpaced(theBoard)
                print('= = = =')
                if f'{letter1.name}{letter2.name}{letter3.name}{letter4.name}' == toGuess:
                    print(f'You won in {tryNum} guess(es)!')
                    time.sleep(3)
                    print('Starting a new game...')
                    time.sleep(3)
                    unfinished = False
            else:
                print(f"You're out of guesses! The word was {toGuess}.")
                time.sleep(3)
                print('Starting a new game...')
                time.sleep(3)
                unfinished = False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
