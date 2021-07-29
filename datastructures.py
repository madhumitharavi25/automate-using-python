import pprint
#import zip
print('Tic-Tac Board')
user = input()
place = input()
theboard = {'top-l':' ','top-m':' ', 'top-r': ' ', 'mid-l':' ', 
'mid-m':' ', 'mid-r': ' ', 'low-l':' ', 'low-m':' ','low-r':' '}
#pprint.pprint(theboard)
def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('------')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('------')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
printBoard(theboard) 
lis1 = list(theboard.values())
lis2 = list(theboard.keys())
if user == 'X' or user == '0':
    if place == 'top-l' or place == 'low-l':
        #lis1.remove(1)
        lis1.insert(0,'X')
        lis1.insert(7,'0')
        print(lis1)
    if place == 'top-m' or place == 'low-m':
        lis1.insert(1,'X')
        lis1.insert(9,'0')
        print(lis1)
    if place == 'top-r' or place == 'low-r':
        lis1.insert(2,'X')
        lis1.insert(9,'0')
        print(lis1)
print(lis1)
print(lis2)
count = {}    
count = dict(zip(lis2, lis1))
print(count)
printBoard(count)





