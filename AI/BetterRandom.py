import random
import sys

sys.path.append("..")  # so other modules can be found in parent dir
from Player import *
from Constants import *
from Construction import CONSTR_STATS
from Ant import UNIT_STATS
from Move import Move
from GameState import *
from AIPlayerUtils import *


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

        moves = listAllLegalMoves(currentState)
        selectedMove = moves[random.randint(0, len(moves) - 1)]

        # don't do a build move if there are already 3+ ants
        numAnts = len(currentState.inventories[currentState.whoseTurn].ants)
        while (selectedMove.moveType == BUILD and numAnts >= 3):
            selectedMove = moves[random.randint(0, len(moves) - 1)]
        self.calculateStateScore(currentState)
        return selectedMove

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
        # method templaste, not implemented
        pass

    stateNode = {
        "parent": None,
        "currentState": None,
        "previousMove": None,  # Move that was taken to get to this state
        "nextMove": None,  # Next best move
        "nextState": None,  # State that will be reached from nextMove
        "stateScore": 0.0
    }

    def calculateStateScore(self, currentState):
        rtrnNumber = 0.0
        rtrnNumber = \
            self.hasPlaerWon(currentState) + \
            self.numOfAnts(currentState) + \
            self.numOfFood(currentState) + \
            self.myQueeenThreat(currentState) + \
            self.enemyQueenThreat(currentState)
        print(rtrnNumber)
        return rtrnNumber

    ##
    # If there is enemy ants close to my queen
    #
    def myQueeenThreat(self, currentState):
        myID = currentState.whoseTurn
        enemyID = 1 - myID

        myInv = currentState.inventories[myID]
        enemyInv = currentState.inventories[enemyID]

        queenCords = myInv.getQueen().coords
        enemyAnts = enemyInv.ants
        closestAnt = None
        for ant in enemyAnts:
            if ant.type != WORKER or QUEEN:
                if closestAnt is None:
                    closestAnt = ant

                if approxDist(ant.coords, queenCords) < approxDist(closestAnt.coords, queenCords):
                    closestAnt = ant
        if closestAnt is None:
            rtrnNumber = 0
        else:
            rtrnNumber = -0.1/approxDist(closestAnt.coords, queenCords)

        return rtrnNumber

    ##
    # If one of my ants is close to the enemy queen
    #
    def enemyQueenThreat(self, currentState):
        myID = currentState.whoseTurn
        enemyID = 1 - myID

        myInv = currentState.inventories[myID]
        enemyInv = currentState.inventories[enemyID]

        enemyQueenCords = enemyInv.getQueen().coords
        myAnts = myInv.ants
        closestAnt = myAnts[0]
        for ant in myAnts:
            if ant.type != WORKER or QUEEN:
                if approxDist(ant.coords, enemyQueenCords) < approxDist(closestAnt.coords, enemyQueenCords):
                    closestAnt = ant

        rtrnNumber = 0.1 / approxDist(closestAnt.coords, enemyQueenCords)
        return rtrnNumber

    def hasPlaerWon(self, currentState):
        if getWinner(currentState) is None:
            return 0.0
        elif getWinner(currentState) == 1:
            return 1.0
        elif getWinner(currentState) == 0:
            return -1.0

    def numOfAnts(self, currentState):
        myInv = currentState.inventories[self.playerId]
        myAnts = myInv.ants

        enemyInv = getEnemyInv(self, currentState)
        enemyAnts = enemyInv.ants

        difference = len(myAnts) - len(enemyAnts)
        rtrnNumber = difference * 0.05
        return rtrnNumber

    def numOfFood(self, currentState):
        enemyFood = getEnemyInv(self, currentState).foodCount
        myFood = len(getCurrPlayerFood(self, currentState))

        difference = (myFood - enemyFood)
        rtrnNumber = difference * 0.05
        return rtrnNumber



