
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from timer import Timer
from random import randint
import numpy
import pygame
import sys
import math



numberOfRows = 6
numberOfColoumns = 7
theLastRow = 5
sizeOfCell =100
heigthOfGameScreen = (numberOfRows+1) * sizeOfCell
widthOfGameScreen = numberOfColoumns * sizeOfCell
sizeOfGameScreen = (widthOfGameScreen, heigthOfGameScreen)

blue=(43, 25, 247)
Color = (163, 26, 33)

pink = (224, 90, 137)
white = (255,255,255)
circleRadius = 50
Green = (0, 166, 50)
yellow = (242, 228, 73)
DRed = (153, 0, 22)

numpyObject = numpy


choice =0
steps=0



LARGE_FONT = ("Verdana", 12)

def HomePage():
    window1 = tk.Tk()
    window1.geometry("500x500")
    window1.rowconfigure(0, minsize=50, weight=1)
    window1.columnconfigure([0,1,2], minsize=50, weight=1)
    label = tk.Label(window1, text="Start Page", font=LARGE_FONT)
    label.pack(pady=80, padx=10)

    def gotoSelectPlayerPage():
        window1.destroy()
        SelectSecondPlayer()

    button = tk.Button(window1, text="Game", width=20, height=3, bg="green", command=gotoSelectPlayerPage)
    button.pack(pady=10)

    def gotoComparisionPage():
        window1.destroy()
        comparisionPage()

    button2 = tk.Button(window1, text="Comparision page", width=20, height=3, bg="green", command=gotoComparisionPage)
    button2.pack()

    window1.mainloop()
def SelectSecondPlayer():
    window3 = tk.Tk()
    window3.geometry("500x500")
    window3.rowconfigure(0, minsize=50, weight=1)
    window3.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label = tk.Label(window3, text="Select Player Page", font=LARGE_FONT)
    label.pack(pady=40, padx=10)
    def gotoHomePage():
        window3.destroy()
        HomePage()
    button1 = tk.Button(window3, text="Back to Home", width=15, height=2, bg="green", command= gotoHomePage)
    v = tk.IntVar()
    button1.pack(pady=10)
    values = {"Easy-Bot (Random Bot) ": "1",
              "Medium-Bot (Min/Max Bot)": "2",
              "Hard-Bot (Pruning Bot)": "3",
              "2 players ": "4"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    def StartGame():
        print(v.get())
        choice = v.get()
        if(choice == 0):
            tk.messagebox.showwarning(title="choose an openning", message="you did not choose anything")
        # elif choice == 1:
        #     PVEasyBot()
        # elif choice == 2:
        #     PVMediumBot()
        # elif choice == 3:
        #     PVHardBot()
        elif choice == 4:
            PVP()


        print(choice)
    for (text, value) in values.items():
        Radiobutton(window3, text=text, variable=v, value=value).pack(side=TOP, ipady=5)
    button = tk.Button(window3, text=" Start Game", width=15, height=2, bg="green", command=StartGame)
    button.pack(pady=10)

    window3.mainloop()


def comparisionPage():
    window2 = tk.Tk()
    window2.geometry("500x500")
    window2.rowconfigure(0, minsize=50, weight=1)
    window2.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label = tk.Label(window2, text="Comparison", font=LARGE_FONT)
    label.pack(pady=10, padx=10)
    def gotoHomePage():
        window2.destroy()
        HomePage()
    button1 = tk.Button(window2, text="Back to Home", bg="green", width=15, height=2,
                        command= gotoHomePage)
    button1.pack()

    output = compare()
    if (len(output) == 0):
        label = tk.Label(window2, text="the Table is empty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
    elif (len(output) > 0):
        random = [0, 0, 0,
                  0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        minmax = [0, 0, 0,
                  0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        pruning = [0, 0, 0,
                   0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        l = len(output)
        rsteps = 0
        msteps = 0
        psteps = 0
        for i in range(l):
            if (output[i][0] == "minmax"):
                minmax[1] += 1
                minmax[0] += output[i][1]
                msteps += output[i][2]
            elif (output[i][0] == "random"):
                random[1] += 1
                random[0] += output[i][1]
                rsteps += output[i][2]
            elif (output[i][0] == "pruning"):
                pruning[1] += 1
                pruning[0] += output[i][1]
                psteps += output[i][2]
        if (random[1] != 0):
            random[2] = rsteps / random[1]
        if (minmax[1] != 0):
            minmax[2] = msteps / minmax[1]
        if (pruning[1] != 0):
            pruning[2] = psteps / pruning[1]
        label2 = tk.Label(window2, text="MinMax BOT: \nWins: " + str(minmax[0]) + " \nNumber of Played Games: "
                                     + str(minmax[1]) + " \naverage number of steps in each game: " + str(
            minmax[2])
                          , font=LARGE_FONT)
        label2.pack(pady=10, padx=10)
        label3 = tk.Label(window2,text="Alpha Beta Pruning BOT: \nWins: "+ str(pruning[0]) +" \nNumber of Played Games: "
                               + str(pruning[1]) + " \naverage number of steps in each game: " + str(pruning[2])
                          , font=LARGE_FONT)
        label3.pack(pady=10, padx=10)
        label4 = tk.Label(window2,text="Random BOT: \nWins: "+ str(random[0]) +" \nNumber of Played Games: "
                               + str(random[1]) +" \naverage number of steps in each game: " + str(random[2])
                          , font=LARGE_FONT)
        label4.pack(pady=10, padx=10)
    def refresh():
        output = compare()
        if (len(output) == 0):
            label = tk.Label(window2, text="the Table is empty", font=LARGE_FONT)
            label.pack(pady=10, padx=10)
        elif(len(output) > 0):
            random = [0, 0, 0,
                          0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
            minmax = [0, 0, 0,
                          0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
            pruning = [0, 0, 0,
                           0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
            l = len(output)
            rsteps = 0
            msteps = 0
            psteps = 0
            for i in range(l):
                if (output[i][0] == "minmax"):
                    minmax[1] += 1
                    minmax[0] += output[i][1]
                    msteps += output[i][2]
                elif (output[i][0] == "random"):
                    random[1] += 1
                    random[0] += output[i][1]
                    rsteps += output[i][2]
                elif (output[i][0] == "pruning"):
                    pruning[1] += 1
                    pruning[0] += output[i][1]
                    psteps += output[i][2]
            if (random[1] != 0):
                random[2] = rsteps / random[1]
            if (minmax[1] != 0):
                minmax[2] = msteps / minmax[1]
            if (pruning[1] != 0):
                pruning[2] = psteps / pruning[1]
            label2["text"] = "MinMax BOT: \nWins: " + str(minmax[0]) + " \nNumber of Played Games: "+ str(minmax[1]) \
                     + " \naverage number of steps in each game: " + str(minmax[2])
            label3["text"] ="Alpha Beta Pruning BOT: \nWins: " + str(
                                      pruning[0]) + " \nNumber of Played Games: "+ str(pruning[1]) \
                    + " \naverage number of steps in each game: " + str(pruning[2])
            label4["text"] = "Random BOT: \nWins: " + str(random[0]) + " \nNumber of Played Games: "\
                     + str(random[1]) + " \naverage number of steps in each game: " + str(random[2])
    button2 = tk.Button(window2, text="refresh", bg="green", width=15, height=2, command=refresh)
    button2.pack()
    # HomePage.destroy
    window2.mainloop()

def compare():
    result = []
    if (sqlite3.connect("track.sqlite3")):
        conn = sqlite3.connect("track.sqlite3")
        cur = conn.cursor()
        cur.execute("select * from history")
        schema = cur.fetchall()
        x = len(schema)
        for i in range(x):
            sum = []
            sum.append(schema[i][1])  # bot
            sum.append(schema[i][2])  # status 0 for lose and 1 for win
            sum.append(schema[i][3])  # number of steps played by the bot
            sum.append(schema[i][4])  # time
            result.append(sum)
        conn.close()
        return result
    else:
        print("Failed")

def boardCreation():
    boardC = numpyObject.zeros((numberOfRows, numberOfColoumns))
    return boardC

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


def boardGUI(currentBoard):
    gameScreen = pygame.display.set_mode(sizeOfGameScreen)
    gameScreen.fill(white)

    for coloumn in range(numberOfColoumns):
        for row in range(numberOfRows):
            pygame.draw.rect(gameScreen, DRed,(coloumn*sizeOfCell,row*sizeOfCell+sizeOfCell,sizeOfCell,sizeOfCell))

            pygame.draw.circle(gameScreen,white,(int(coloumn*sizeOfCell+sizeOfCell/2),int(row*sizeOfCell+sizeOfCell+sizeOfCell/2)),circleRadius)

    for coloumn in range(numberOfColoumns):
        for row in range(numberOfRows):
            if currentBoard[row][coloumn] == 1:
                pygame.draw.circle(gameScreen, Green, (
                int(coloumn * sizeOfCell + sizeOfCell / 2),int(heigthOfGameScreen-int(row * sizeOfCell  + sizeOfCell / 2))) , circleRadius)

            elif currentBoard[row][coloumn] == 2:
                pygame.draw.circle(gameScreen, yellow, (
                int(coloumn * sizeOfCell + sizeOfCell / 2), int(heigthOfGameScreen-int(row * sizeOfCell  + sizeOfCell / 2))), circleRadius)
    pygame.display.update()












def PVP():
    #newFont = font = pygame.font.Font("monospace", 75)
    gameScreen = pygame.display.set_mode(sizeOfGameScreen)
    pygame.init()
    newBoard = boardCreation()

    boardGUI(newBoard)
    pygame.display.update()
    gameOver = False
    whosTurn = randint(0, 1)
    i = 0
    while not gameOver:

        for anyEvent in pygame.event.get():
            if anyEvent.type == pygame.QUIT:
                pygame.quit()
                


            elif anyEvent.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gameScreen,white,(0,0,widthOfGameScreen,sizeOfCell))
                mousePosition = anyEvent.pos[0]
                if whosTurn == 0:
                    pygame.draw.circle(gameScreen,Green,(mousePosition,int(sizeOfCell/2)),circleRadius)
                else:
                    pygame.draw.circle(gameScreen, yellow, (mousePosition, int(sizeOfCell / 2)), circleRadius)
                pygame.display.update()


            if anyEvent.type == pygame.MOUSEBUTTONDOWN:


                if whosTurn == 0:
                    play = anyEvent.pos[0]
                    coloumn= int(math.floor(play/sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 1)

                        if winCheck(newBoard, 1):
                            #text = fontCreation.render("Green won the game!!",1,blue)

                            #gameScreen.blit(text,(50,50))



                            gameOver = True
        # #


                else:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 2) #this line put the disc in the board
                        if winCheck(newBoard, 2):
                            #text = fontCreation.render("Yellow won the game!!", 1, blue)
                            #gameScreen.blit(text, (50, 50))
                            gameOver = True
                boardGUI(newBoard)
                whosTurn+= 1
                whosTurn%=2

        if gameOver:
            for anyEvent in pygame.event.get():
                if anyEvent.type == pygame.QUIT:
                    pygame.quit()
            pygame.time.wait(1000)
            pygame.quit()


# def PVEasyBot():
#     # newFont = font = pygame.font.Font("monospace", 75)
#     gameScreen = pygame.display.set_mode(sizeOfGameScreen)
#     pygame.init()
#     newBoard = boardCreation()
#
#     boardGUI(newBoard)
#     pygame.display.update()
#     gameOver = False
#     whosTurn = randint(0, 1)
#     i = 0
#     while not gameOver:
#
#         for anyEvent in pygame.event.get():
#             if anyEvent.type == pygame.QUIT:
#                 pygame.quit()
#
#
#
#             elif anyEvent.type == pygame.MOUSEMOTION:
#                 pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
#                 mousePosition = anyEvent.pos[0]
#                 if whosTurn == 0:
#                     pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 else:
#                     pygame.draw.circle(gameScreen, yellow, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 pygame.display.update()
#
#             if anyEvent.type == pygame.MOUSEBUTTONDOWN:
#
#                 if whosTurn == 0:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 1)
#
#                         if winCheck(newBoard, 1):
#                             # text = fontCreation.render("Green won the game!!",1,blue)
#
#                             # gameScreen.blit(text,(50,50))
#
#                             gameOver = True
#                 # #
#
#                 else:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 2)
#                         if winCheck(newBoard, 2):
#                             # text = fontCreation.render("Yellow won the game!!", 1, blue)
#                             # gameScreen.blit(text, (50, 50))
#                             gameOver = True
#                 boardGUI(newBoard)
#                 whosTurn += 1
#                 whosTurn %= 2
#
#         if gameOver:
#             for anyEvent in pygame.event.get():
#                 if anyEvent.type == pygame.QUIT:
#                     pygame.quit()
#             pygame.time.wait(1000)
#             pygame.quit()
#
# def PVMediumBot():
#     # newFont = font = pygame.font.Font("monospace", 75)
#     gameScreen = pygame.display.set_mode(sizeOfGameScreen)
#     pygame.init()
#     newBoard = boardCreation()
#
#     boardGUI(newBoard)
#     pygame.display.update()
#     gameOver = False
#     whosTurn = randint(0, 1)
#     i = 0
#     while not gameOver:
#
#         for anyEvent in pygame.event.get():
#             if anyEvent.type == pygame.QUIT:
#                 pygame.quit()
#
#
#
#             elif anyEvent.type == pygame.MOUSEMOTION:
#                 pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
#                 mousePosition = anyEvent.pos[0]
#                 if whosTurn == 0:
#                     pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 else:
#                     pygame.draw.circle(gameScreen, yellow, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 pygame.display.update()
#
#             if anyEvent.type == pygame.MOUSEBUTTONDOWN:
#
#                 if whosTurn == 0:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 1)
#
#                         if winCheck(newBoard, 1):
#                             # text = fontCreation.render("Green won the game!!",1,blue)
#
#                             # gameScreen.blit(text,(50,50))
#
#                             gameOver = True
#                 # #
#
#                 else:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 2)
#                         if winCheck(newBoard, 2):
#                             # text = fontCreation.render("Yellow won the game!!", 1, blue)
#                             # gameScreen.blit(text, (50, 50))
#                             gameOver = True
#                 boardGUI(newBoard)
#                 whosTurn += 1
#                 whosTurn %= 2
#
#         if gameOver:
#             for anyEvent in pygame.event.get():
#                 if anyEvent.type == pygame.QUIT:
#                     pygame.quit()
#             pygame.time.wait(1000)
#             pygame.quit()
#
#
#
# def PVHardBot():
#     # newFont = font = pygame.font.Font("monospace", 75)
#     gameScreen = pygame.display.set_mode(sizeOfGameScreen)
#     pygame.init()
#     newBoard = boardCreation()
#
#     boardGUI(newBoard)
#     pygame.display.update()
#     gameOver = False
#     whosTurn = randint(0, 1)
#     i = 0
#     while not gameOver:
#
#         for anyEvent in pygame.event.get():
#             if anyEvent.type == pygame.QUIT:
#                 pygame.quit()
#
#
#
#             elif anyEvent.type == pygame.MOUSEMOTION:
#                 pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
#                 mousePosition = anyEvent.pos[0]
#                 if whosTurn == 0:
#                     pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 else:
#                     pygame.draw.circle(gameScreen, yellow, (mousePosition, int(sizeOfCell / 2)), circleRadius)
#                 pygame.display.update()
#
#             if anyEvent.type == pygame.MOUSEBUTTONDOWN:
#
#                 if whosTurn == 0:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 1)
#
#                         if winCheck(newBoard, 1):
#                             # text = fontCreation.render("Green won the game!!",1,blue)
#
#                             # gameScreen.blit(text,(50,50))
#
#                             gameOver = True
#                 # #
#
#                 else:
#                     play = anyEvent.pos[0]
#                     coloumn = int(math.floor(play / sizeOfCell))
#
#                     if fullColoumnChecking(newBoard, coloumn):
#                         freeSlot = freeSlotFunction(newBoard, coloumn)
#                         discDrop(newBoard, freeSlot, coloumn, 2)
#                         if winCheck(newBoard, 2):
#                             # text = fontCreation.render("Yellow won the game!!", 1, blue)
#                             # gameScreen.blit(text, (50, 50))
#                             gameOver = True
#                 boardGUI(newBoard)
#                 whosTurn += 1
#                 whosTurn %= 2
#
#         if gameOver:
#             for anyEvent in pygame.event.get():
#                 if anyEvent.type == pygame.QUIT:
#                     pygame.quit()
#             pygame.time.wait(1000)
#             pygame.quit()
#
# def winning_move(board, piece):
# 	# Check horizontal locations for win
# 	for c in range(numberOfColoumns-3):
# 		for r in range(numberOfRows):
# 			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
# 				return True
#
# 	# Check vertical locations for win
# 	for c in range(numberOfColoumns):
# 		for r in range(numberOfRows-3):
# 			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
# 				return True
#
# 	# Check positively sloped diaganols
# 	for c in range(numberOfColoumns-3):
# 		for r in range(ROW_COUNT-3):
# 			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
# 				return True
#
# 	# Check negatively sloped diaganols
# 	for c in range(numberOfColoumns-3):
# 		for r in range(3, ROW_COUNT):
# 			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
# 				return True
#
# def is_terminal_node(board):
#     valid_locations = []
#     for col in range(numberOfColoumns):
#         if freeSlotFunction(board, col):
#             valid_locations.append(col)
# 	return winning_move(board, 1) or winning_move(board, 2) or len(valid_locations) == 0
#
#
# def score_position(board, piece):
# 	score = 0
#
# 	## Score center column
# 	center_array = [int(i) for i in list(board[:, numberOfColoumns//2])]
# 	center_count = center_array.count(piece)
# 	score += center_count * 3
#
# 	## Score Horizontal
# 	for r in range(numberOfRows):
# 		row_array = [int(i) for i in list(board[r,:])]
# 		for c in range(numberOfColoumns-3):
# 			window = row_array[c:c+WINDOW_LENGTH]
# 			score += evaluate_window(window, piece)
#
# 	## Score Vertical
# 	for c in range(numberOfColoumns):
# 		col_array = [int(i) for i in list(board[:,c])]
# 		for r in range(ROW_COUNT-3):
# 			window = col_array[r:r+WINDOW_LENGTH]
# 			score += evaluate_window(window, piece)
#
# 	## Score posiive sloped diagonal
# 	for r in range(ROW_COUNT-3):
# 		for c in range(numberOfColoumns-3):
# 			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += evaluate_window(window, piece)
#
# 	for r in range(ROW_COUNT-3):
# 		for c in range(numberOfColoumns-3):
# 			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += evaluate_window(window, piece)
#
# 	return score
#
# def pruning(board, depth, alpha, beta, maximizingPlayer):
# 	#valid_locations = get_valid_locations(board)
#     valid_locations = []
#     for col in range(numberOfColoumns):
#         if freeSlotFunction(board, col):
#             valid_locations.append(col)
#
# 	is_terminal = is_terminal_node(board)
# 	if depth == 0 or is_terminal:
# 		if is_terminal:
# 			if winning_move(board, 2):
# 				return (None, 100000000000000)
# 			elif winning_move(board, 1):
# 				return (None, -10000000000000)
# 			else: # Game is over, no more valid moves
# 				return (None, 0)
# 		else: # Depth is zero
# 			return (None, score_position(board, 2))
# 	if maximizingPlayer:
# 		value = -math.inf
# 		column = random.choice(valid_locations)
# 		for col in valid_locations:
# 			row = get_next_open_row(board, col)
# 			b_copy = board.copy()
# 			drop_piece(b_copy, row, col, AI_PIECE)
# 			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
# 			if new_score > value:
# 				value = new_score
# 				column = col
# 			alpha = max(alpha, value)
# 			if alpha >= beta:
# 				break
# 		return column, value
#
# 	else: # Minimizing player
# 		value = math.inf
# 		column = random.choice(valid_locations)
# 		for col in valid_locations:
# 			row = get_next_open_row(board, col)
# 			b_copy = board.copy()
# 			drop_piece(b_copy, row, col, PLAYER_PIECE)
# 			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
# 			if new_score < value:
# 				value = new_score
# 				column = col
# 			beta = min(beta, value)
# 			if alpha >= beta:
# 				break
# 		return column, value



HomePage()





