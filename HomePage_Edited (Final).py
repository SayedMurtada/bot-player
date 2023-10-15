
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from timer import Timer
from random import randint
import random
import numpy
import pygame
import math
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches

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
winner=""


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

    button2 = tk.Button(window1, text="Comparision page", width=20, height=3, bg="green", command=comparisionPage)
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
    values = {"very-Easy Bot ": "1",
              "Easy Bot ": "2",
              "Medium Bot ": "3",
              "Medium-hard Bot":"4",
              "2 players ": "5"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    def StartGame():
        choice = v.get()
        if(choice == 0):
            tk.messagebox.showwarning(title="choose an openning", message="you did not choose anything")
        if choice == 1:
            veryeasyAI()
        if choice == 2:
            EasyAI()
        if choice == 3:
            MedBOT()
        if choice == 4:
            MedHard()
        if choice ==5:
            PVP()

    for (text, value) in values.items():
        Radiobutton(window3, text=text, variable= v, value=value).pack(side=TOP, ipady=5)
    button = tk.Button(window3, text=" Start Game", width=15, height=2, bg="green", command=StartGame)
    button.pack(pady=10)

    window3.mainloop()


def comparisionPage():
    output, numberofgames = compare()
    if (len(output) == 0):
        label = tk.messagebox.showinfo(text="the Table is empty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
    elif (len(output) > 0):
        lowestgamesnumber = 0
        leng = len(numberofgames)
        for i in range(leng):
            print(numberofgames[i])
            if (i == 0):
                lowestgamesnumber = numberofgames[i]
            elif (lowestgamesnumber > numberofgames[i]):
                lowestgamesnumber = numberofgames[i]
        print("lowest ",lowestgamesnumber)
        random = [0, 0, 0,
                  0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        scoreheuristic = [0, 0, 0, 0]
        minmax = [0, 0, 0,
                  0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        pruning = [0, 0, 0,
                   0]  # 0 for number of wins and 1 for number of played games and 2 for average number of steps and 3 for avg time
        l = len(output)
        rsteps = 0
        shsteps = 0
        msteps = 0
        psteps = 0
        rtime = 0
        shtime = 0
        mtime = 0
        ptime = 0
        print("minmax1 = ",pruning[1])
        for i in range(l):
            if (output[i][0] == "minmax" and minmax[1] < lowestgamesnumber):
                minmax[1] += 1
                minmax[0] += output[i][1]
                msteps += output[i][2]
                mtime += output[i][3]
            elif (output[i][0] == "random" and random[1] < lowestgamesnumber):
                random[1] += 1
                random[0] += output[i][1]
                rsteps += output[i][2]
                rtime += output[i][3]
            elif (output[i][0] == "pruning" and pruning[1] < lowestgamesnumber):
                pruning[1] += 1
                pruning[0] += output[i][1]
                psteps += output[i][2]
                ptime += output[i][3]
            elif (output[i][0] == "scoreheuristic" and scoreheuristic[1] < lowestgamesnumber):
                scoreheuristic[1] += 1
                scoreheuristic[0] += output[i][1]
                shsteps += output[i][2]
                shtime += output[i][3]
        if (random[1] != 0):
            random[2] = rsteps / random[1]
            random[3] = rtime / rsteps
        if (minmax[1] != 0):
            minmax[2] = msteps / minmax[1]
            minmax[3] = mtime / msteps
        if (pruning[1] != 0):
            pruning[2] = psteps / pruning[1]
            pruning[3] = ptime / psteps
        if (scoreheuristic[1] != 0):
            scoreheuristic[2] = shsteps / scoreheuristic[1]
            scoreheuristic[3] = shtime / shsteps
        print("minmax1 = ", pruning[1])
        Noter=""
        Noteh=""
        Notemm=""
        Notep=""
        if(random[3]/1000000 > 1):
            random[3]= random[3]/1000000
            Noter = "Time in method random is in seconds"
        elif(random[3]/1000000 *1000>1):
            random[3] = random[3] / 1000000 * 1000
            Noter = "Time in method random is in milli seconds"
        else:
            Noter= "Time in method random is in micro seconds"

        if (scoreheuristic[3] / 1000000 > 1):
            scoreheuristic[3] = scoreheuristic[3] / 1000000
            Noteh = "Time in method Score heuristic is in seconds"
        elif (scoreheuristic[3] / 1000000 * 1000 > 1):
            scoreheuristic[3] = scoreheuristic[3] / 1000000 * 1000
            Noteh = "Time in method Score heuristic is in milli seconds"
        else:
            Noteh= "Time in method Score heuristic is in micro seconds"

        if (minmax[3] / 1000000 > 1):
            minmax[3] = minmax[3] / 1000000
            Notemm = "Time in method minmax is in seconds"
        elif (minmax[3] / 1000000 * 1000 > 1):
            minmax[3] = minmax[3] / 1000000 * 1000
            Notemm = "Time in method minmax is in milli seconds"
        else:
            Notemm= "Time in method minmax is in micro seconds"

        if (pruning[3] / 1000000 >= 1):
            pruning[3] = pruning[3] / 1000000
            Notep = "Time in method pruning is in seconds"
        elif (pruning[3] / 1000000 * 1000 > 1):
            pruning[3] = pruning[3] / 1000000 * 1000
            Notep = "Time in method pruning is in milli seconds"
        else:
            Notep= "Time in method pruning is in micro seconds"

        Highestnumber = 0
        if(random[3]>scoreheuristic[3] and random[3]>minmax[3] and random[3]>pruning[3]):
            Highestnumber = random[3]
        if(scoreheuristic[3] > random[3] and scoreheuristic[3] > minmax[3] and scoreheuristic[3] > pruning[3]):
            Highestnumber = scoreheuristic[3]
        if (minmax[3] > random[3] and minmax[3] > scoreheuristic[3] and minmax[3] > pruning[3]):
            Highestnumber = minmax[3]
        if (pruning[3] > random[3] and pruning[3] > scoreheuristic[3] and pruning[3] > minmax[3]):
            Highestnumber = pruning[3]
        subjects =["Random Bot", "Score Heuristic Bot", "Min/Max Bot", "Min/Max with Alpha Beta Pruning"]
        indx = numpy.arange(len(subjects))
        print(sum(numberofgames))
        print(numberofgames)

        iterate = 0
        if(Highestnumber<10):
            iterate=1
        elif(Highestnumber<100):
            iterate = 10
        elif (Highestnumber < 1000):
            iterate = 50
        else:
            iterate = 100

        Games = numpy.arange(0,Highestnumber,iterate)
        TotalstepsAvgPerGame = [random[2], scoreheuristic[2], minmax[2], pruning[2]]
        TotaltimeavgPerGame = [random[3], scoreheuristic[3], minmax[3], pruning[3]]
        wins = [random[0], scoreheuristic[0], minmax[0], pruning[0]]
        barw = 0.25

        fig, z = plot.subplots()
        barsteps = z.bar(indx + barw, TotalstepsAvgPerGame, barw, color="blue", label='Average number of steps per game')
        bartime = z.bar(indx + barw*2, TotaltimeavgPerGame, barw, color="orange", label='Total Average time per move in all games')
        barwins = z.bar(indx + barw*3 , wins, barw, color="green", label='Number of wins')
        z.set_xticks(indx+ barw*2)
        z.set_xticklabels(subjects)

        z.set_yticks(Games)
        z.set_yticklabels(Games)

        greenp = mpatches.Patch(color='green', label='Number of wins')
        orangep = mpatches.Patch(color='orange', label='Total Average time per move in all games')
        bluep = mpatches.Patch(color='blue', label='Average number of steps per game')
        redp = mpatches.Patch(color='White', label=Noter)
        whitep = mpatches.Patch(color='White', label=Noteh)
        mmpatch = mpatches.Patch(color='White', label=Notemm)
        ppatch = mpatches.Patch(color='White', label=Notep)
        gpatch = mpatches.Patch(color='White', label="Total number of Games used in this comparison is "+str(lowestgamesnumber))
        z.legend(handles=[greenp, orangep, bluep, redp, whitep, mmpatch, ppatch, gpatch])
        # z.legend()
        def insert_data_labels(bars):
            for bar in bars:
                bar_height = bar.get_height()
                z.annotate('{0:.0f}'.format(bar.get_height()),
                            xy=(bar.get_x() + bar.get_width() / 2, bar_height),
                            xytext=(0, 3),
                            textcoords='offset points',
                            ha='center',
                            va='bottom'
                            )

        insert_data_labels(barsteps)
        insert_data_labels(bartime)
        insert_data_labels(barwins)
        plot.show()

        print("Random", random)
        print("Score heuristic", scoreheuristic)
        print("Min/Max", minmax)
        print("Pruning", pruning)

def compare():
    result = []
    ra, heu, mima, pr = 0,0,0,0
    NumberofGames=[] # 0 for random, 1 for heuristic score, 2 for MinMax, 3 for pruning
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
            sum.append(schema[i][4])  # time taken by the Bot to make moves
            result.append(sum)
            if (schema[i][1] == "minmax"):
                mima += 1
            elif (schema[i][1] == "random"):
                ra += 1
            elif (schema[i][1] == "pruning"):
                pr += 1
            elif (schema[i][1] == "scoreheuristic"):
                heu += 1
        conn.close()
        NumberofGames.append(ra)
        NumberofGames.append(heu)
        NumberofGames.append(mima)
        NumberofGames.append(pr)
        return result, NumberofGames
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
            if (currentBoard[row][coloumn] == disc
                    and currentBoard[row][coloumn + 1] == disc
                    and currentBoard[row][coloumn + 2] == disc
                    and currentBoard[row][coloumn + 3] == disc):
                return True

    for row in range(numberOfRows-3):
        for coloumn in range(numberOfColoumns):
            if currentBoard[row][coloumn] == disc \
                    and currentBoard[row+1][coloumn] == disc \
                    and currentBoard[row+2][coloumn] == disc \
                    and currentBoard[row+3][coloumn] == disc:
                return True

    for row in range(numberOfRows-3):
        for coloumn in range(numberOfColoumns-3):
            if currentBoard[row][coloumn] == disc \
                    and currentBoard[row+1][coloumn+1] == disc \
                    and currentBoard[row+2][coloumn+2] == disc \
                    and currentBoard[row+3][coloumn+3] == disc:
                return True

    for row in range(3,numberOfRows):
        for coloumn in range(numberOfColoumns-3):
            if currentBoard[row][coloumn] == disc \
                    and currentBoard[row-1][coloumn+1] == disc \
                    and currentBoard[row-2][coloumn+2] == disc \
                    and currentBoard[row-3][coloumn+3] == disc:
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




def stateEvaluation(state,disc):
    HueristicScore = 0
    currentDisc = 1
    if disc == 1:
        currentDisc = 2
    if state.count(disc) == 4:
        HueristicScore += 100
    elif state.count(disc) == 3 and state.count(0) ==1:
        HueristicScore+=10
    elif state.count(disc) ==2 and state.count(0) ==2:
        HueristicScore+=5
    elif state.count(currentDisc) == 3 and state.count(0) == 1:
        HueristicScore -= 25
    return HueristicScore



def positionScore(currentBoard,disc):
    HueristicScore = 0

    centerArray = [int(i) for i in list(currentBoard[:,numberOfColoumns//2])]
    centerMove = centerArray.count(disc)
    HueristicScore+=centerMove*6


    for row in range(numberOfRows):
        rowArray = [int(i) for i in list(currentBoard[row,:])]
        for coloumn in range(numberOfColoumns-3):
            state= rowArray[coloumn:coloumn+4]
            HueristicScore+= stateEvaluation(state,disc)

    for coloumn in range(numberOfColoumns):
        coloumnArray = [int(i) for i in list(currentBoard[:,coloumn])]
        for row in range(numberOfRows-3):
            state = coloumnArray[row:row+4]
            HueristicScore+= stateEvaluation(state,disc)

    for row in range(numberOfRows-3):
        for coloumn in range(numberOfColoumns-3):
            state = [currentBoard[row+i][coloumn+i] for i in range(4)]
            HueristicScore+= stateEvaluation(state,disc)

    for row in range(numberOfRows-3):
         for coloumn in range(numberOfColoumns-3):
             state = [currentBoard[row+3-i][coloumn+i] for i in range(4)]
         HueristicScore+= stateEvaluation(state,disc)


    return HueristicScore


def bestMove(curretBoard,disc):
    Scores=[]
    freeSlots = allFreeSlots(curretBoard)
    bestScore = 0
    bestColoumn = random.choice(freeSlots)
    for coloumn in freeSlots:
        slot = freeSlotFunction(curretBoard,coloumn)
        tempBoard = curretBoard.copy()
        discDrop(tempBoard,slot,coloumn,disc)
        score = positionScore(tempBoard,disc)
        Scores.append(score)
        if score >bestScore:
            bestScore = score
            bestColoumn = coloumn
    return bestColoumn



def allFreeSlots(currentBoard):
    freeSlots = []
    for coloumn in range(numberOfColoumns):
        if fullColoumnChecking(currentBoard,coloumn):
            freeSlots.append(coloumn)
    return freeSlots



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
                            winner = "Player1"
        # #


                else:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 2)
                        if winCheck(newBoard, 2):
                            #text = fontCreation.render("Yellow won the game!!", 1, blue)
                            #gameScreen.blit(text, (50, 50))
                            gameOver = True
                            winner ="Player 2"
                boardGUI(newBoard)
                whosTurn+= 1
                whosTurn%=2

        if gameOver:
            tk.messagebox.showinfo(title="Winner", message=winner + " Wins")
            # pygame.time.wait(2500)
            pygame.quit()


def veryeasyAI():
    AItime = 0
    AIsteps = 0
    # newFont = font = pygame.font.Font("monospace", 75)
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
                pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
                mousePosition = anyEvent.pos[0]
                if whosTurn == 0:
                    pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
                pygame.display.update()

            if anyEvent.type == pygame.MOUSEBUTTONDOWN:

                if whosTurn == 0:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 1)
                        whosTurn += 1
                        whosTurn %= 2
                        boardGUI(newBoard)

                        if winCheck(newBoard, 1):
                            # text = fontCreation.render("Green won the game!!",1,blue)

                            # gameScreen.blit(text,(50,50))
                            winner = "Player"
                            gameOver = True
                # #

        if whosTurn ==1 and not gameOver:
            t = Timer()
            t.start()
            coloumn = randint(0,numberOfColoumns-1)
            AIsteps +=1

            if fullColoumnChecking(newBoard, coloumn):
                time = t.stop()
                AItime += time
                freeSlot = freeSlotFunction(newBoard, coloumn)
                discDrop(newBoard, freeSlot, coloumn, 2)
                if winCheck(newBoard, 2):
                            # text = fontCreation.render("Yellow won the game!!", 1, blue)
                            # gameScreen.blit(text, (50, 50))
                    gameOver = True
                    winner = "Bot"
                boardGUI(newBoard)
                whosTurn += 1
                whosTurn %= 2

        if gameOver:
            try:
                if (sqlite3.connect("Data.sqlite3")):
                    conn = sqlite3.connect("track.sqlite3")
                    cur = conn.cursor()
                    if (winner == "Bot"):
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("random",1,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    else:
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("random",0,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    conn.commit()
                    conn.close()
                else:
                    print("Failed")
            except (Exception) as error:
                print(error)
            tk.messagebox.showinfo(title="Winner", message=winner + " Wins")
            # pygame.time.wait(2500)
            pygame.quit()

def EasyAI():
    AItime = 0
    AIsteps = 0
    # newFont = font = pygame.font.Font("monospace", 75)
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
                pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
                mousePosition = anyEvent.pos[0]
                if whosTurn == 0:
                    pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
                pygame.display.update()

            if anyEvent.type == pygame.MOUSEBUTTONDOWN:

                if whosTurn == 0:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 1)
                        whosTurn += 1
                        whosTurn %= 2
                        boardGUI(newBoard)

                        if winCheck(newBoard, 1):
                            # text = fontCreation.render("Green won the game!!",1,blue)

                            # gameScreen.blit(text,(50,50))
                            winner = "Player"
                            gameOver = True
                # #

        if whosTurn ==1 and not gameOver:
            AIsteps +=1
            t = Timer()
            t.start()
            coloumn = bestMove(newBoard,2)


            if fullColoumnChecking(newBoard, coloumn):
                time = t.stop()
                AItime += time
                freeSlot = freeSlotFunction(newBoard, coloumn)
                discDrop(newBoard, freeSlot, coloumn, 2)
                if winCheck(newBoard, 2):
                            # text = fontCreation.render("Yellow won the game!!", 1, blue)
                            # gameScreen.blit(text, (50, 50))
                    gameOver = True
                    winner = "Bot"
                boardGUI(newBoard)
                whosTurn += 1
                whosTurn %= 2

        if gameOver:
            try:
                if (sqlite3.connect("Data.sqlite3")):
                    conn = sqlite3.connect("track.sqlite3")
                    cur = conn.cursor()
                    if (winner == "Bot"):
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("scoreheuristic",1,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    else:
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("scoreheuristic",0,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    conn.commit()
                    conn.close()
                else:
                    print("Failed")
            except (Exception) as error:
                print(error)
            tk.messagebox.showinfo(title="Winner", message=winner + " Wins")
            # pygame.time.wait(2500)
            pygame.quit()


def is_terminal_node(board):
	return winCheck(board, 1) or winCheck(board, 2) or len(allFreeSlots(board)) == 0


def minmaxBestMove(currentboard, depth, maxplayer):
    freeslots = allFreeSlots(currentboard)
    is_terminal = is_terminal_node(currentboard)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winCheck(currentboard, 2):
                return (None, 100000000000000)
            elif winCheck(currentboard, 1):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, positionScore(currentboard, 2))
    if maxplayer:
        value = -math.inf
        column = random.choice(freeslots)
        for col in freeslots:
            row = freeSlotFunction(currentboard, col)
            b_copy = currentboard.copy()
            discDrop(b_copy, row, col, 2)
            newscore = minmaxBestMove(b_copy, depth - 1, False)[1]
            if newscore > value:
                value = newscore
                column = col

        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(freeslots)
        for col in freeslots:
            row = freeSlotFunction(currentboard, col)
            b_copy = currentboard.copy()
            discDrop(b_copy, row, col, 1)
            newscore = minmaxBestMove(b_copy, depth - 1, True)[1]
            if newscore < value:
                value = newscore
                column = col

        return column, value


def minmaxPruningBestMove(currentboard, depth, alpha, beta, maxplayer):
    freeslots = allFreeSlots(currentboard)
    is_terminal = is_terminal_node(currentboard)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winCheck(currentboard, 2):
                return (None, 100000000000000)
            elif winCheck(currentboard, 1):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, positionScore(currentboard, 2))
    if maxplayer:
        value = -math.inf
        column = random.choice(freeslots)
        for col in freeslots:
            row = freeSlotFunction(currentboard, col)
            b_copy = currentboard.copy()
            discDrop(b_copy, row, col, 2)
            newscore = minmaxPruningBestMove(b_copy, depth - 1, alpha, beta, False)[1]
            if newscore > value:
                value = newscore
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(freeslots)
        for col in freeslots:
            row = freeSlotFunction(currentboard, col)
            b_copy = currentboard.copy()
            discDrop(b_copy, row, col, 1)
            newscore = minmaxPruningBestMove(b_copy, depth - 1, alpha, beta, True)[1]
            if newscore < value:
                value = newscore
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def MedBOT():
    AItime = 0
    AIsteps = 0
    # newFont = font = pygame.font.Font("monospace", 75)
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
                pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
                mousePosition = anyEvent.pos[0]
                if whosTurn == 0:
                    pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
                pygame.display.update()

            if anyEvent.type == pygame.MOUSEBUTTONDOWN:

                if whosTurn == 0:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 1)
                        whosTurn += 1
                        whosTurn %= 2
                        boardGUI(newBoard)

                        if winCheck(newBoard, 1):
                            # text = fontCreation.render("Green won the game!!",1,blue)

                            # gameScreen.blit(text,(50,50))
                            winner = "Player"
                            gameOver = True
                # #

        if whosTurn == 1 and not gameOver:
            # coloumn = bestMove(newBoard, 2)
            AIsteps += 1
            t = Timer()
            t.start()
            coloumn, minimax_score = minmaxBestMove(newBoard, 5, True)
            if fullColoumnChecking(newBoard, coloumn):
                time = t.stop()
                AItime +=time
                freeSlot = freeSlotFunction(newBoard, coloumn)
                discDrop(newBoard, freeSlot, coloumn, 2)
                if winCheck(newBoard, 2):
                    # text = fontCreation.render("Yellow won the game!!", 1, blue)
                    # gameScreen.blit(text, (50, 50))
                    gameOver = True
                    winner = "Bot"
                boardGUI(newBoard)
                whosTurn += 1
                whosTurn %= 2

        if gameOver:
            try:
                if (sqlite3.connect("Data.sqlite3")):
                    conn = sqlite3.connect("track.sqlite3")
                    cur = conn.cursor()
                    if (winner == "Bot"):
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("minmax",1,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    else:
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("minmax",0,' + str(
                            AIsteps) + ',' + str(AItime * 1000000) + ');')
                    conn.commit()
                    conn.close()
                else:
                    print("Failed")
            except (Exception) as error:
                print(error)
            tk.messagebox.showinfo(title="Winner", message=winner + " Wins")
            # pygame.time.wait(2500)
            pygame.quit()


def MedHard():
    AItime = 0
    AIsteps = 0
    # newFont = font = pygame.font.Font("monospace", 75)
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
                pygame.draw.rect(gameScreen, white, (0, 0, widthOfGameScreen, sizeOfCell))
                mousePosition = anyEvent.pos[0]
                if whosTurn == 0:
                    pygame.draw.circle(gameScreen, Green, (mousePosition, int(sizeOfCell / 2)), circleRadius)
                pygame.display.update()

            if anyEvent.type == pygame.MOUSEBUTTONDOWN:

                if whosTurn == 0:
                    play = anyEvent.pos[0]
                    coloumn = int(math.floor(play / sizeOfCell))

                    if fullColoumnChecking(newBoard, coloumn):
                        freeSlot = freeSlotFunction(newBoard, coloumn)
                        discDrop(newBoard, freeSlot, coloumn, 1)
                        whosTurn += 1
                        whosTurn %= 2
                        boardGUI(newBoard)

                        if winCheck(newBoard, 1):
                            # text = fontCreation.render("Green won the game!!",1,blue)

                            # gameScreen.blit(text,(50,50))
                            winner = "Player"
                            gameOver = True
                # #

        if whosTurn == 1 and not gameOver:
            # coloumn = bestMove(newBoard, 2)
            AIsteps += 1
            t = Timer()
            t.start()
            coloumn, minimax_score = minmaxPruningBestMove(newBoard, 5, -math.inf, math.inf, True)
            if fullColoumnChecking(newBoard, coloumn):
                time=t.stop()
                AItime += time
                freeSlot = freeSlotFunction(newBoard, coloumn)
                discDrop(newBoard, freeSlot, coloumn, 2)
                if winCheck(newBoard, 2):
                    # text = fontCreation.render("Yellow won the game!!", 1, blue)
                    # gameScreen.blit(text, (50, 50))
                    gameOver = True
                    winner="Bot"
                boardGUI(newBoard)
                whosTurn += 1
                whosTurn %= 2

        if gameOver:
            try:
                if (sqlite3.connect("Data.sqlite3")):
                    conn = sqlite3.connect("track.sqlite3")
                    cur = conn.cursor()
                    if(winner=="Bot"):
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("pruning",1,'+str(AIsteps)+','+str(AItime*1000000)+');')
                    else:
                        cur.execute('INSERT INTO history (bot,status,steps,time) VALUES("pruning",0,'+str(AIsteps)+','+str(AItime*1000000)+');')
                    conn.commit()
                    conn.close()
                else:
                    print("Failed")
            except (Exception) as error:
                print(error)
            tk.messagebox.showinfo(title="Winner", message=winner+" Wins")
            # pygame.time.wait(2500)
            pygame.quit()

HomePage()





