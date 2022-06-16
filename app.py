#!/usr/bin/env python3

import time
import csv
from termcolor import colored, cprint
import os
import sys

from Node import Node
from Scorer import Scorer
from heapq import *


height = 0
width = 0
opened = []
closed = []
maze = [[]]
finalPath = []

moves_x = [1, -1, 0, 0]
moves_y = [0 , 0, 1,-1]

terminal_h = os.get_terminal_size().lines + 10

def getNode(x, y):
    for e in opened:
        if e.x == x and e.y == y:
            return e
    
    for e in closed:
        if e.x == x and e.y == y:
            return e

    return None

def wipe():
    print("\033[F"*(terminal_h))

def getMaze(fileName):
    global height, width
    isCsv = fileName.endswith('csv')
    maze = None
    if isCsv:
        with open(fileName,  encoding="utf8") as f:
            maze = []
            for row in csv.reader(f):
                maze.append( [int(x) for x in row] )
    else:
        with open(fileName) as f:
            maze = []
            for row in f.readlines():
                maze.append( [int(x) for x in row.strip()] )

    height = len(maze)
    width = len(maze[0])

    return maze

def validMove(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        if maze[y][x] == 1:
            n = getNode(x, y)
            if n == None or n not in closed:
                return True
    return False

def getColored(x, y):
    n = getNode(x, y)

    if (x == 0 and y == 0) or (x == (width-1) and y == (height-1)):
        coloredText = colored(" ", 'magenta', attrs=['reverse']) 
    elif n in finalPath:
        coloredText = colored("X", 'green', attrs=['reverse']) 
    elif n in closed:
        # coloredText = " "
        coloredText = colored("X", 'red', attrs=['reverse']) 
    elif n in opened:
        coloredText = colored("X", 'cyan', attrs=['reverse']) 
    elif maze[y][x] == 1:
        coloredText = " "
        coloredText = colored(" ", 'white', attrs=['reverse']) 

    else:
        coloredText = colored(" ", 'grey', attrs=['reverse']) 

    return coloredText

tries = 0

def display(currentNode):
    buildPathFromCurrent(currentNode)
    wipe()
    for y, _ in enumerate(maze):
        for x, _ in enumerate(maze[y]):

            coloredText = getColored(x, y)
            print(coloredText, end='')
        print('')
    print('')

def printPath(currentNode):
    if currentNode == None:
        return
    printPath(currentNode.getParent())  

    print(currentNode.idNode)


def buildPathFromCurrent(currentNode):
    global finalPath
    finalPath = []
    current = currentNode
    finalPath.append(current)
    while current.getParent() != None:
        finalPath.append(current.getParent())
        current = current.getParent()

def smallest():

    if len(opened) == 1:
        return heappop(opened)

    smallests = []
    for i in range(min(5, len(opened))):
        smallests.append(heappop(opened))

    s = smallests[0]

    for s_t in smallests:
        if s_t.getH() < s.getH():
            s = s_t
    for s_t in smallests:
        if s_t != s:
            heappush(opened, s_t)

    return s


def solve(entrypoint, exitnode, frames):
    global tries
    current = None
    entrypoint = Scorer.score(None, entrypoint, exitnode)
    heappush(opened, entrypoint)

    while len(opened) > 0:
        tries += 1
        current = smallest()
        heappush(closed, current)

       
        if current.getX() == exitnode.getX() and current.getY() == exitnode.getY():
            print("END")
            display(current)
            return True

        for i, _ in enumerate(moves_x):
            nextX = current.getX() + moves_x[i]
            nextY = current.getY() + moves_y[i]

            if validMove(nextX, nextY):
                # print("VALID")
                nextNode = getNode(nextX, nextY)
                if nextNode == None:
                    nextNode = Node(nextX, nextY)
                    heappush(opened, nextNode)

                nextNode = Scorer.score(current, nextNode, exitnode)

        if tries % frames == 0:
            display(current)

    print("NO SOLUTION")
    return False

maze = getMaze(sys.argv[1])
if len(sys.argv) == 3:
    frames = int(sys.argv[2])
else:
    frames = 50
entrypoint = Node(0,0)
exitnode = Node(width - 1, height - 1)
solve(entrypoint, exitnode, frames)
