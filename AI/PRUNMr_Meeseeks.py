import random
import sys
import time
sys.path.append("..")  #so other modules can be found in parent dir
from Player import *
from Constants import *
from Construction import CONSTR_STATS
from Ant import UNIT_STATS
from Move import Move
from GameState import *
from AIPlayerUtils import *


##
#AIPlayer
#Description: The responsbility of this class is to interact with the game by
#deciding a valid move based on a given game state. This class has methods that
#will be implemented by students in Dr. Nuxoll's AI course.
#
#Variables:
#   playerId - The id of the player.
##
class AIPlayer(Player):

    #__init__
    #Description: Creates a new Player
    #
    #Parameters:
    #   inputPlayerId - The id to give the new player (int)
    #   cpy           - whether the player is a copy (when playing itself)
    ##
    def __init__(self, inputPlayerId):
        super(AIPlayer,self).__init__(inputPlayerId, "Mr. Meeseeks")
        self.depthLimit = 1
        self.food = []
        self.homes = []

    ##
    #getPlacement
    #
    #Description: called during setup phase for each Construction that
    #   must be placed by the player.  These items are: 1 Anthill on
    #   the player's side; 1 tunnel on player's side; 9 grass on the
    #   player's side; and 2 food on the enemy's side.
    #
    #Parameters:
    #   construction - the Construction to be placed.
    #   currentState - the state of the game at this point in time.
    #
    #Return: The coordinates of where the construction is to be placed
    ##
    def getPlacement(self, currentState):
        numToPlace = 0
        #implemented by students to return their next move
        if currentState.phase == SETUP_PHASE_1:    #stuff on my side
            numToPlace = 11
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    #Choose any x location
                    x = random.randint(0, 9)
                    #Choose any y location on your side of the board
                    y = random.randint(0, 3)
                    #Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        #Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        elif currentState.phase == SETUP_PHASE_2:   #stuff on foe's side
            numToPlace = 2
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    #Choose any x location
                    x = random.randint(0, 9)
                    #Choose any y location on enemy side of the board
                    y = random.randint(6, 9)
                    #Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        #Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        else:
            return [(0, 0)]

    ##
    #getMove
    #Description: Gets the next move from the Player.
    #
    #Parameters:
    #   currentState - The state of the current game waiting for the player's move (GameState)
    #
    #Return: The Move to be made
    ##
    def getMove(self, currentState):
        cpyState = currentState.fastclone()
        self.foods = getConstrList(currentState,None,(FOOD,))
        self.homes = getConstrList(currentState,currentState.whoseTurn,(ANTHILL, TUNNEL,))

        move = self.startBestMoveSearch(cpyState, cpyState.whoseTurn)

        return move

    ##
    #getAttack
    #Description: Gets the attack to be made from the Player
    #
    #Parameters:
    #   currentState - A clone of the current state (GameState)
    #   attackingAnt - The ant currently making the attack (Ant)
    #   enemyLocation - The Locations of the Enemies that can be attacked (Location[])
    ##
    def getAttack(self, currentState, attackingAnt, enemyLocations):
        #Attack a random enemy.
        return enemyLocations[random.randint(0, len(enemyLocations) - 1)]

    def startBestMoveSearch(self,state,me):
        moves = []
        currScore = self.scoreState(state,me)
        moves.extend(listAllMovementMoves(state))
        moves.extend(listAllBuildMoves(state))
        nextStates = []
        for move in moves:
            nextStates.append(getNextState(state,move))
        nextNodes = []
        for i in range(0,len(moves)):
            nextNodes.append( self.getBestMove(moves[i],nextStates[i],1,me) )
        selectMove = Move(END,None,None)
        for node in nextNodes:
            if node["score"] >= currScore:
                selectMove = node["move"]
                currScore = node["score"]
        return selectMove


    def getBestMove(self,move,state,depth,me):
        thisNode = {"move": move, "state": state, "score": self.scoreState(state,me)}
        moves = []
        moves.extend(listAllMovementMoves(state))
        moves.extend(listAllBuildMoves(state))
        if len(moves) == 0: return thisNode
        nextStates = []
        for move in moves:
            nextStates.append(getNextState(state,move))
        if (depth == self.depthLimit):
            scores = []
            for state in nextStates:
                scores.append(self.scoreState(state,me))
            thisNode["score"] = max(scores)
        else:
            nextNodes = []
            for i in range(0,len(moves)):
                nextNodes.append( self.getBestMove(moves[i],nextStates[i],depth+1,me) )

            nodeListScore = self.scoreNodeList(nextNodes,me)
            if thisNode["score"] <= nodeListScore:
                thisNode["score"] = nodeListScore
        return thisNode

    def scoreNodeList(self, nodes, me):
        scores = []
        for node in nodes:
            scores.append(node["score"])
        return max(scores)
    ##
    #scoreState
    #Description: scores the advantage of the current state form 1.0 to -1.0,
    #higher numbers advantaging the 'me' player
    #
    #Parameters:
    #   gameState - gameState to analyze
    ##
    def scoreState(self, gameState, me):
        playerFoodGross = gameState.inventories[me].foodCount
        playerFoodScaled = playerFoodGross/11.0
        score = playerFoodScaled
        workers = getAntList(gameState,me,(WORKER,))

        if score < 1.0:
            if len(workers) < 2: score = score-.1
            for worker in workers:
                if worker.carrying:
                    score = score + .01
                    stepsToHomes = (approxDist(worker.coords,self.homes[0].coords),approxDist(worker.coords,self.homes[1].coords))
                    minSteps = min(stepsToHomes)
                    score = score + .01/(1.0+minSteps)
                else:
                    stepsToFoods = (approxDist(worker.coords,self.foods[0].coords),approxDist(worker.coords,self.foods[1].coords),\
                                    approxDist(worker.coords,self.foods[2].coords),approxDist(worker.coords,self.foods[3].coords))
                    minSteps = min(stepsToFoods)
                    score = score + .01/(1.0+minSteps)

        return score


    ##
    #registerWin
    #
    # This agent doens't learn
    #
    def registerWin(self, hasWon):
        #method templaste, not implemented
        pass

def testMeeseek():
    gameState = GameState.getBasicState()
    gameState.inventories[0].foodCount = 11
    AI = AIPlayer(PLAYER_ONE)
    winstate = AI.scoreState(gameState,0)
    if winstate != 1:
        print('You have an error in your scoreState, not recording 11 food as victory')
    else:
        print("passed unit test")

testMeeseek()
