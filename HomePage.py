import numpy
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from timer import Timer
# numpyObject = numpy
# gameOver = False
# whosTurn = 0
# numberOfRows = 6
# numberOfColoumns = 7
# theLastRow = 5
choice =0

# def connect():
#     if (sqlite3.connect("track.sqlite3")):
#         result = []
#         conn = sqlite3.connect("track.sqlite3")
#         cur = conn.cursor()
#         cur.execute("select * from history")
#         schema = cur.fetchall()
#         x = len(schema)
#         for i in range(x):
#             sum = []
#
#         conn.close()
#         return result
#     else:
#         print("Failed")


LARGE_FONT = ("Verdana", 12)

def HomePage():
    window1 = tk.Tk()
    window1.rowconfigure(0, minsize=50, weight=1)
    window1.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label = tk.Label(window1, text="Start Page", font=LARGE_FONT)
    label.pack(pady=10, padx=10)

    def gotoSelectPlayerPage():
        window1.destroy()
        SelectSecondPlayer()

    button = tk.Button(window1, text="Game",
                       command=gotoSelectPlayerPage)
    button.pack()

    def gotoComparisionPage():
        window1.destroy()
        comparisionPage()

    button2 = tk.Button(window1, text="Comparision page",command=gotoComparisionPage)
    button2.pack()

    window1.mainloop()
def SelectSecondPlayer():
    window3 = tk.Tk()
    window3.rowconfigure(0, minsize=50, weight=1)
    window3.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label = tk.Label(window3, text="Select Player Page", font=LARGE_FONT)
    label.pack(pady=10, padx=10)
    def gotoHomePage():
        window3.destroy()
        HomePage()
    button1 = tk.Button(window3, text="Back to Home",
                        command= gotoHomePage)
    v = tk.IntVar()
    button1.pack()
    values = {"Random Bot ": "1",
              "Min/Max Bot ": "2",
              "Alpha Beta Pruning Bot ": "3",
              "another person ": "4"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    def StartGame():
        print(v.get())
        choice = v.get()
        if(choice == 0):
            tk.messagebox.showwarning(title="choose an openning", message="you did not choose anything")
        print(choice)
    for (text, value) in values.items():
        Radiobutton(window3, text=text, variable= v,
                    value=value).pack(side=TOP, ipady=5)
    button = tk.Button(window3, text=" Start Game", command=StartGame)
    button.pack()

    window3.mainloop()


def comparisionPage():
    window2 = tk.Tk()
    window2.rowconfigure(0, minsize=50, weight=1)
    window2.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label = tk.Label(window2, text="Comparison", font=LARGE_FONT)
    label.pack(pady=10, padx=10)
    def gotoHomePage():
        window2.destroy()
        HomePage()
    button1 = tk.Button(window2, text="Back to Home",
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
    button2 = tk.Button(window2, text="refresh", command=refresh)
    button2.pack()
    HomePage.destroy
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

HomePage()
# t=Timer()
# t.start()
# a=0
# for i in range(10000):
#     a += 4**4
#
# e = t.stop()
# print(type(e))



# def boardCreation():
#     board = numpyObject.zeros((numberOfRows, numberOfColoumns))
#     return board
#
# def discDrop(currentBoard , row, slot, disc):
#     currentBoard[row][slot] = disc
#
# def freeSlotFunction(currentBoard, slot):
#      for row in range(numberOfRows):
#         if currentBoard[row][slot] == 0:
#             return row
#
# def fullColoumnChecking(currentBoard, slot):
#     return currentBoard[theLastRow][slot] == 0
#
# def winCheck(currentBoard,disc):
#     for row in range(numberOfRows):
#         for coloumn in range(numberOfColoumns-3):
#             if currentBoard[row][coloumn] == disc and currentBoard[row][coloumn + 1] == disc and currentBoard[row][coloumn + 2] == disc and currentBoard[row][
#                 coloumn + 3] == disc:
#                 return True
#
#     for row in range(numberOfRows-3):
#         for coloumn in range(numberOfColoumns):
#             if currentBoard[row][coloumn] == disc and currentBoard[row+1][coloumn] == disc and currentBoard[row+2][
#                 coloumn] == disc and currentBoard[row+3][
#                 coloumn] == disc:
#                 return True
#
#     for row in range(numberOfRows-3):
#         for coloumn in range(numberOfColoumns-3):
#             if currentBoard[row][coloumn] == disc and currentBoard[row+1][coloumn+1] == disc and currentBoard[row+2][
#                 coloumn+2] == disc and currentBoard[row+3][
#                 coloumn+3] == disc:
#                 return True
#
#     for row in range(3,numberOfRows):
#         for coloumn in range(numberOfColoumns-3):
#             if currentBoard[row][coloumn] == disc and currentBoard[row-1][coloumn+1] == disc and currentBoard[row-2][
#                 coloumn+2] == disc and currentBoard[row-3][coloumn+3] == disc:
#                 return True





# newBoard = boardCreation()
# print(newBoard)
# while not gameOver:
#     if whosTurn == 0 :
#         play= int (input("Player 1 Turn ( Enter a number between 0 and 6):"))
#
#         if (fullColoumnChecking(newBoard,play)):
#             freeSlot = freeSlotFunction(newBoard,play)
#             discDrop(newBoard,freeSlot,play,1)
#
#             if winCheck(newBoard, 1):
#                print("Yaaaay Player 1 won the game!!!!")
#                gameOver = True
#
#         print(numpyObject.flip(newBoard, 0))
#
#
#
#     else:
#         play = int (input("Player 2 Turn ( Enter a number between 0 and 6"))
#         if (fullColoumnChecking(newBoard, play)):
#             freeSlot = freeSlotFunction(newBoard, play)
#             discDrop(newBoard, freeSlot, play, 2)
#             if winCheck(newBoard, 2):
#                 print("Yaaaay Player 2 won the game!!!!")
#                 gameOver = True
#         print(numpyObject.flip(newBoard,0))
#     whosTurn+=1
#     whosTurn%=2





