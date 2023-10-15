import numpy

numpyObject = numpy
gameOver = False
whosTurn = 0
numberOfRows = 6
numberOfColoumns = 7
theLastRow = 5






def boardCreation():
    board = numpyObject.zeros((numberOfRows, numberOfColoumns))
    return board

def discDrop(currentBoard , row, slot, disc):
    currentBoard[row][slot] = disc

def freeSlotFunction(currentBoard, slot):
     for row in range(numberOfRows):
        if currentBoard[row][slot] == 0:
            return row

def fullColoumnChecking(currentBoard, slot):
    return currentBoard[theLastRow][slot] == 0

def winCheck(currentBoard,disc):
    for row in range(numberOfRows):
        for coloumn in range(numberOfColoumns-3):
            if currentBoard[row][coloumn] == disc and currentBoard[row][coloumn + 1] == disc and currentBoard[row][coloumn + 2] == disc and currentBoard[row][
                coloumn + 3] == disc:
                return True

    for row in range(numberOfRows-3):
        for coloumn in range(numberOfColoumns):
            if currentBoard[row][coloumn] == disc and currentBoard[row+1][coloumn] == disc and currentBoard[row+2][
                coloumn] == disc and currentBoard[row+3][
                coloumn] == disc:
                return True

    for row in range(numberOfRows-3):
        for coloumn in range(numberOfColoumns-3):
            if currentBoard[row][coloumn] == disc and currentBoard[row+1][coloumn+1] == disc and currentBoard[row+2][
                coloumn+2] == disc and currentBoard[row+3][
                coloumn+3] == disc:
                return True

    for row in range(3,numberOfRows):
        for coloumn in range(numberOfColoumns-3):
            if currentBoard[row][coloumn] == disc and currentBoard[row-1][coloumn+1] == disc and currentBoard[row-2][
                coloumn+2] == disc and currentBoard[row-3][
                coloumn+3] == disc:
                return True





newBoard = boardCreation()
print(newBoard)
while not gameOver:
    if whosTurn == 0 :
        play= int (input("Player 1 Turn ( Enter a number between 0 and 6):"))

        if (fullColoumnChecking(newBoard,play)):
            freeSlot = freeSlotFunction(newBoard,play)
            discDrop(newBoard,freeSlot,play,1)

            if winCheck(newBoard, 1):
               print("Yaaaay Player 1 won the game!!!!")
               gameOver = True

        print(numpyObject.flip(newBoard, 0))



    else:
        play = int (input("Player 2 Turn ( Enter a number between 0 and 6"))
        if (fullColoumnChecking(newBoard, play)):
            freeSlot = freeSlotFunction(newBoard, play)
            discDrop(newBoard, freeSlot, play, 2)
            if winCheck(newBoard, 2):
                print("Yaaaay Player 2 won the game!!!!")
                gameOver = True
        print(numpyObject.flip(newBoard,0))
    whosTurn+=1
    whosTurn%=2





