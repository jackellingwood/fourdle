# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
};

def addColor(s, color):
    return colors[color] + s + colors['none']

letter1 = ''
letter2 = ''
letter3 = ''
letter4 = ''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {addColor(name, "cyan")}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {addColor(name, "blue")}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
