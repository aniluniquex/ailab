# Global Variable i
i = 0

def Monkey_go_box(x, y):
    global i
    i = i + 1
    print('step:', i, 'monkey slave', x, 'Go to ' + y)

def Monkey_move_box(x, y):
    global i
    i = i + 1
    print('step:', i, 'monkey takes the box from', x, 'and delivers it to ' + y)

def Monkey_on_box():
    global i
    i = i + 1
    print('step:', i, 'Monkey climbs up the box')

def Monkey_get_banana():
    global i
    i = i + 1
    print('step:', i, 'Monkey picks a banana')

import sys

# Read the input operating parameters
codeIn = sys.stdin.read()
codeInList = codeIn.split()

# The operating parameters indicate the locations of monkey, banana, and box respectively.
monkey = codeInList[0]
banana = codeInList[1]
box = codeInList[2]

print('The steps are as follows:')

# Use the least steps to complete the monkey picking banana task
Monkey_go_box(monkey, box)
Monkey_move_box(box, banana)
Monkey_on_box()
Monkey_get_banana()
