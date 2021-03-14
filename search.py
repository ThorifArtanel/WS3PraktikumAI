# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue

def search(maze):
    fringe = queue.Queue()
    fringe.put(maze.getStart())
    explored = []
    parent = {}

    while not fringe.empty():
        current = fringe.get()
        explored.append(current)
        row = current[0]
        col = current[1]
        if maze.isObjective(row, col):
            print("found" + "ROW: " + str(row) + " COL: " + str(col))
            return compileEndResult(maze.getStart(), (row, col), parent)

        print("row: " + str(row) + " col: " + str(col))
        newFringe = maze.getNeighbors(row, col)
        for x, y in enumerate(newFringe):
            if not isExist(y, explored):
                fringe.put(y)
                parent[y] = current

    for x, y in enumerate(explored):
        row = y[0]
        col = y[1]
        print("row: " + str(row) + " col: " + str(col))

    return []


def isExist(newFringe, explored):
    for x, y in enumerate(explored):
        if y == newFringe:
            return True

    return False


def compileEndResult(initialState, endState, parent):
    endResult = []
    endResult.insert(0, endState)

    while initialState != endState:
        for item in parent.items():
            if item[0] == endState:
                endResult.insert(0, item[1])
                endState = item[1]
                break

    return endResult
