import random
import sys
import unittest
import time

sys.path.append("..")  # so other modules can be found in parent dir
from Player import *
from Constants import *
from Construction import CONSTR_STATS
from Ant import UNIT_STATS
from Move import Move
from GameState import *
from AIPlayerUtils import *
from SearchTree import *
from StateNode import *


##
# AIPlayer
# Description: The responsibility of this class is to interact with the game by
# deciding a valid move based on a given game state. This class has methods that
# will be implemented by students in Dr. Nuxoll's AI course.
#
# Variables:
#   playerId - The id of the player.
##
class AIPlayer(Player):

    # __init__
    # Description: Creates a new Player
    #
    # Parameters:
    #   inputPlayerId - The id to give the new player (int)
    #   cpy           - whether the player is a copy (when playing itself)
    ##
    def __init__(self, inputPlayerId):
        super(AIPlayer, self).__init__(inputPlayerId, "Better Random")
        self.searchTree = SearchTree()
        self.searchTree.depthLimit = 2
        self.myTunnel = None
        self.myFood = None

    ##
    # getPlacement
    #
    # Description: called during setup phase for each Construction that
    #   must be placed by the player.  These items are: 1 Anthill on
    #   the player's side; 1 tunnel on player's side; 9 grass on the
    #   player's side; and 2 food on the enemy's side.
    #
    # Parameters:
    #   construction - the Construction to be placed.
    #   currentState - the state of the game at this point in time.
    #
    # Return: The coordinates of where the construction is to be placed
    ##
    def getPlacement(self, currentState):
        numToPlace = 0
        # implemented by students to return their next move
        if currentState.phase == SETUP_PHASE_1:  # stuff on my side
            numToPlace = 11
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    # Choose any x location
                    x = random.randint(0, 9)
                    # Choose any y location on your side of the board
                    y = random.randint(0, 3)
                    # Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        # Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        elif currentState.phase == SETUP_PHASE_2:  # stuff on foe's side
            numToPlace = 2
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    # Choose any x location
                    x = random.randint(0, 9)
                    # Choose any y location on enemy side of the board
                    y = random.randint(6, 9)
                    # Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        # Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        else:
            return [(0, 0)]

    ##
    # getMove
    # Description: Gets the next move from the Player.
    #
    # Parameters:
    #   currentState - The state of the current game waiting for the player's move (GameState)
    #
    # Return: The Move to be made
    ##
    def getMove(self, currentState):
        me = currentState.whoseTurn
        foods = getConstrList(currentState, None, (FOOD,))

        if self.myTunnel is None:
            self.myTunnel = getConstrList(currentState, me, (TUNNEL,))[0]
        if self.myFood == None:
            closest = 1000
            for food in foods:
                dist = approxDist(self.myTunnel.coords, food.coords)
                if (dist < closest):
                    self.myFood = food
                    closest = dist

        myInv = getCurrPlayerInventory(currentState)
        # if the queen is on the anthill move her
        myQueen = myInv.getQueen()
        self.searchTree.top = StateNode(currentState, None, None, None, 0)
        self.searchTree.top.subNodes = self.RecursiveFindMove(currentState, 0)
        bestScore = -100
        bestNode = self.searchTree.top
        for node in self.searchTree.top.subNodes:
            if node.move is not None:
                if node.score > bestScore:
                    bestNode = node
                    bestScore = node.score
        return bestNode.move

    ##
    # getAttack
    # Description: Gets the attack to be made from the Player
    #
    # Parameters:
    #   currentState - A clone of the current state (GameState)
    #   attackingAnt - The ant currently making the attack (Ant)
    #   enemyLocation - The Locations of the Enemies that can be attacked (Location[])
    ##
    def getAttack(self, currentState, attackingAnt, enemyLocations):
        # Attack a random enemy.
        return enemyLocations[random.randint(0, len(enemyLocations) - 1)]

    ##
    # registerWin
    #
    # This agent doens't learn
    #
    def registerWin(self, hasWon):
        # method template, not implemented
        pass

    def RecursiveFindMove(self, GameState, currentDepth):
        if currentDepth <= self.searchTree.depthLimit:
            nodes = []
            states = []  # List of next states being generated by each move
            node = StateNode(GameState, None, 0, None, currentDepth, None, None)
            moves = listAllLegalMoves(GameState)  # List of all legal moves from that state
            for move in moves:
                states.append(getNextState(GameState, move))
            if len(states) < 15:
                x = len(states)
            else:
                x = 15
            for i in range(0, x):
                newNode = StateNode(states[i], GameState, 0, moves[i], currentDepth, node, None)
                newNode.score = self.calculateStateScore(states[i])
                nodesToCalculate = self.RecursiveFindMove(states[i], currentDepth + 1)
                if nodesToCalculate is not None:
                    newNode.subNodes = nodesToCalculate
                    node.score = self.BestNodeInList(nodesToCalculate)
                nodes.append(newNode)
            return nodes
        else:
            return None

    # Revised Version of Get Next State
    def getNextState(self, currentState, move):
        # variables I will need
        myGameState = currentState.fastclone()
        myInv = getCurrPlayerInventory(myGameState)
        me = myGameState.whoseTurn
        myAnts = myInv.ants
        myTunnels = myInv.getTunnels()
        myAntHill = myInv.getAnthill()

        # If enemy ant is on my anthill or tunnel update capture health
        ant = getAntAt(myGameState, myAntHill.coords)
        if ant is not None:
            if ant.player != me:
                myAntHill.captureHealth -= 1

        # If an ant is built update list of ants
        antTypes = [WORKER, DRONE, SOLDIER, R_SOLDIER]
        if move.moveType == BUILD:
            if move.buildType in antTypes:
                ant = Ant(myInv.getAnthill().coords, move.buildType, me)
                myInv.ants.append(ant)
                # Update food count depending on ant built
                if move.buildType == WORKER:
                    myInv.foodCount -= 1
                elif move.buildType == DRONE or move.buildType == R_SOLDIER:
                    myInv.foodCount -= 2
                elif move.buildType == SOLDIER:
                    myInv.foodCount -= 3
            # ants are no longer allowed to build tunnels, so this is an error
            elif move.buildType == TUNNEL:
                print("Attempted tunnel build in getNextState()")
                return currentState

        # If an ant is moved update their coordinates and has moved
        elif move.moveType == MOVE_ANT:
            newCoord = move.coordList[-1]
            startingCoord = move.coordList[0]
            for ant in myAnts:
                if ant.coords == startingCoord:
                    ant.coords = newCoord
                    # TODO: should this be set true? Design decision
                    ant.hasMoved = False
                    attackable = listAttackable(ant.coords, UNIT_STATS[ant.type][RANGE])
                    for coord in attackable:
                        foundAnt = getAntAt(myGameState, coord)
                        if foundAnt is not None:  # If ant is adjacent my ant
                            if foundAnt.player != me:  # if the ant is not me
                                foundAnt.health = foundAnt.health - UNIT_STATS[ant.type][ATTACK]  # attack
                                # If an enemy is attacked and looses all its health remove it from the other players
                                # inventory
                                if foundAnt.health <= 0:
                                    myGameState.inventories[1 - me].ants.remove(foundAnt)
                                # If attacked an ant already don't attack any more
                                break
        return myGameState

    # Filter that looked for moves that wasn't towards the enemy side
    # TODO delete because not used
    def DroneFilter(self, node):
        currentState = node.nextState
        prevState = node.previousState

        curDrones = getAntList(currentState, currentState.whoseTurn, (DRONE,))
        prevDrone = getAntList(prevState, currentState.whoseTurn, (DRONE,))

        tunnel = getConstrList(currentState, 1 - currentState.whoseTurn, (TUNNEL,))
        enemyWorker = getAntList(currentState, 1 - currentState.whoseTurn, (WORKER,))

        if len(enemyWorker) < 0:
            return True
        elif (len(curDrones) > 0) and (len(prevDrone) > 0):
            if curDrones[0].coords == tunnel[0].coords:
                return True
            if curDrones[0].coords != prevDrone[0].coords:
                dist1 = approxDist(curDrones[0].coords, tunnel[0].coords)
                dist2 = approxDist(prevDrone[0].coords, tunnel[0].coords)
                if dist1 > dist2:
                    return False
        return True

    # Filter the queen's movements
    # TODO Delete because not used
    def QueenFilter(self, node):
        currentState = node.nextState
        prevState = node.previousState

        curQueen = getAntList(currentState, currentState.whoseTurn, (QUEEN,))[0]
        prevQueen = getAntList(prevState, currentState.whoseTurn, (QUEEN,))[0]

        hill = getConstrList(currentState, currentState.whoseTurn, (ANTHILL,))[0]
        if curQueen.coords != hill.coords and prevQueen.coords == hill.coords:
            return True
        return False

    # Evaluates a list of nodes and
    #
    def evaluateNodeList(self, nodes):
        if nodes is not None:
            if len(nodes) > 0:
                sum = 0
                for node in nodes:
                    if node is not None:
                        sum += node.score
                average = sum / (len(nodes))
                return average
            else:
                return 0
        else:
            return 0  # meaning no nodes in list

    # Finds the best Node in the List of Nodes
    # Based on score
    def BestNodeInList(self, nodes):
        if nodes is not None:
            if len(nodes) > 0:
                best = -100
                for node in nodes:
                    if node.score > best:
                        best = node.score
                return best
            else:
                return 0
        else:
            return 0


    def calculateStateScore(self, currentState):
        rtrnNumber = self.hasPlaerWon(currentState)
        if rtrnNumber == 10:
            return rtrnNumber
        else:
            rtrnNumber = self.workerAnts(currentState) + self.numOfFood(currentState) + self.numOfAnts(currentState) + \
                         self.hasPlaerWon(currentState) + \
                         self.DronTunnelAttack(currentState)
        return rtrnNumber

    ##
    # If there is enemy ants close to my queen
    #
    def myQueeenThreat(self, currentState):
        myID = currentState.whoseTurn
        enemyID = 1 - myID

        myInv = currentState.inventories[myID]
        enemyInv = currentState.inventories[enemyID]

        antHillCords = getConstrList(currentState, currentState.whoseTurn, (ANTHILL,))[0]
        queenCords = myInv.getQueen().coords
        enemyAnts = enemyInv.ants
        closestAnt = None
        for ant in enemyAnts:
            if ant.type is not QUEEN and ant.type is not WORKER:
                if closestAnt is None:
                    closestAnt = ant

                if approxDist(ant.coords, queenCords) < approxDist(closestAnt.coords, queenCords):
                    closestAnt = ant
        if closestAnt is None:
            rtrnNumber = 0
        else:
            rtrnNumber = -0.5 / approxDist(closestAnt.coords, queenCords)
        if antHillCords.coords == queenCords:
            rtrnNumber = rtrnNumber + -1

        # print("Queen Threat: " + str(rtrnNumber))
        return rtrnNumber

    ##
    # If one of my ants is close to the enemy queen
    #
    def enemyQueenThreat(self, currentState):
        myID = currentState.whoseTurn
        enemyID = 1 - myID

        myInv = currentState.inventories[myID]
        enemyInv = currentState.inventories[enemyID]
        enemyQueen = enemyInv.getQueen()
        if enemyQueen is not None:
            enemyQueenCords = enemyQueen.coords
            myAnts = myInv.ants
            if len(myAnts) is not 0:
                closestAnt = myAnts[0]
                for ant in myAnts:
                    if ant.type is not QUEEN and ant.type is not WORKER:
                        if approxDist(ant.coords, enemyQueenCords) \
                                < approxDist(closestAnt.coords, enemyQueenCords):
                            closestAnt = ant

            if closestAnt.type is not QUEEN and closestAnt.type is not WORKER:
                rtrnNumber = 0.5 / approxDist(closestAnt.coords, enemyQueenCords)
            else:
                rtrnNumber = 0.00

            if enemyQueen.health > 10:
                rtrnNumber += 0.1 / enemyQueen.health
        else:
            rtrnNumber = 1

        # print("Enemy Queen Threat: " + str(rtrnNumber))
        return rtrnNumber

    def hasPlaerWon(self, currentState):
        if getWinner(currentState) is None:
            return 0.0
        elif getWinner(currentState) == 1:
            return 10.0
        elif getWinner(currentState) == 0:
            return -10.0

    def DronTunnelAttack(self, currentState):
        myInv = currentState.inventories[currentState.whoseTurn]
        myDrones = getAntList(currentState, currentState.whoseTurn, (SOLDIER, R_SOLDIER,))
        enemyAnts = getAntList(currentState, 1 - currentState.whoseTurn, (WORKER,))
        if len(enemyAnts) > 0:
            if len(myDrones) > 0:
                tunnel = getConstrList(currentState, 1 - currentState.whoseTurn, (TUNNEL,))
                for drone in myDrones:
                    dist = approxDist(drone.coords, tunnel[0].coords)
                    if dist == 0:
                        return 0.06
                    else:
                        return 0.05 / dist
        else:
            return self.DroneAttack(currentState)
        return 0

    def DroneAttack(self, currentState):
        myInv = currentState.inventories[currentState.whoseTurn]
        myDrones = getAntList(currentState, currentState.whoseTurn, (SOLDIER, R_SOLDIER,))
        enemyAnts = getAntList(currentState, 1 - currentState.whoseTurn, (WORKER,))
        if len(enemyAnts) > 0:
            return -1
        else:
            if len(myDrones) > 0:
                if len(enemyAnts) > 0:
                    workerAnt = enemyAnts[0]
                    for ant in enemyAnts:
                        if ant is WORKER:
                            workerAnt = ant
                    rtrnNumber = 0
                    dist = 100
                    bestDistance = 10000
                    for drone in myDrones:
                        dist = approxDist(drone.coords, workerAnt.coords)
                        if dist < bestDistance:
                            bestDistance = dist
                    if bestDistance is 0:
                        rtrnNumber += 0.06
                    else:
                        rtrnNumber += 0.05 / bestDistance
                    return rtrnNumber
                else:
                    return self.enemyQueenThreat(currentState)
        return 0

    def numOfAnts(self, currentState):
        myInv = currentState.inventories[self.playerId]
        myAnts = myInv.ants

        enemyInv = getEnemyInv(self, currentState)
        enemyAnts = enemyInv.ants
        enemyWorkers = getAntList(currentState, 1 - currentState.whoseTurn, (WORKER,))

        drones = getAntList(currentState, currentState.whoseTurn, (R_SOLDIER, SOLDIER,))
        soldiers = getAntList(currentState, currentState.whoseTurn, (SOLDIER,))
        rtrnNumber = 0
        if len(drones) == 1:
            rtrnNumber = rtrnNumber + 1
        elif len(drones) > 0 and len(drones) <= 3:
            rtrnNumber = rtrnNumber + (1 * len(drones))

        if len(soldiers) > 0:
            rtrnNumber = (0.5 * len(soldiers))

        if len(enemyWorkers) == 0:
            rtrnNumber = rtrnNumber + 1
        else:
            rtrnNumber = rtrnNumber + -0.1

        # print("Number of Ants: " + str(rtrnNumber))
        return rtrnNumber

    ##
    # numOfFood
    #
    # Calculates the amount of food that the human has
    def numOfFood(self, currentState):
        enemyFood = getEnemyInv(self, currentState).foodCount
        myInv = currentState.inventories[currentState.whoseTurn]

        if myInv.foodCount == 0:
            rtrnNumber = -2
        else:
            rtrnNumber = myInv.foodCount * 0.5
        # print("Food Count: " + str(rtrnNumber))
        return rtrnNumber

    def workerAnts(self, currentState):
        me = currentState.whoseTurn
        foods = getConstrList(currentState, None, (FOOD,))

        # Get of Tunnel
        self.myTunnel = getConstrList(currentState, me, (TUNNEL,))[0]
        # Find Closest Food
        closest = 1000
        for food in foods:
            dist = approxDist(self.myTunnel.coords, food.coords)
            if dist < closest:
                self.myFood = food
                closest = dist
        myFood = self.myFood
        myTunnel = self.myTunnel
        myWorkers = getAntList(currentState, currentState.whoseTurn, (WORKER,))
        rtrnNumber = 0
        # Calculate a evaluation score based on the worker ants
        if len(myWorkers) is not 0:
            for worker in myWorkers:
                if worker.carrying:
                    rtrnNumber += 0.2
                    if worker.coords == myTunnel.coords:
                        dist = 0
                    else:
                        dist = approxDist(worker.coords, myTunnel.coords)
                        rtrnNumber += 0.2 / dist
                        return rtrnNumber
                else:
                    if worker.coords == myFood.coords:
                        dist = 0
                    else:
                        dist = approxDist(worker.coords, myFood.coords)
                        rtrnNumber += 0.2 / dist
                        return rtrnNumber

                if dist is 0:
                    rtrnNumber += 0.08
                else:
                    rtrnNumber += 0.1 / dist
        else:
            rtrnNumber = -0.5
        return rtrnNumber


#  Unit Test Class
class BetterRandomUnitTests(unittest.TestCase):

    def TestRecursiveFindMove(self):
        self.assertEquals(0, 0)
