import random
import sys
import time

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
# Description: The responsbility of this class is to interact with the game by
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
        super(AIPlayer, self).__init__(inputPlayerId, "Mr. Meeseeks")
        self.depthLimit = 3
        self.foods = []
        self.homes = []
        self.playerIndex = None

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
        # implemented by students to return their next move
        if currentState.phase == SETUP_PHASE_1:  # stuff on my side
            num_to_place = 11
            moves = []
            for i in range(0, num_to_place):
                move = None
                while move is None:
                    # Choose any x location
                    x = random.randint(0, 9)
                    # Choose any y location on your side of the board
                    y = random.randint(0, 3)
                    # Set the move if this space is empty
                    if currentState.board[x][y].constr is None and (x, y) not in moves:
                        move = (x, y)
                        # Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        elif currentState.phase == SETUP_PHASE_2:  # stuff on foe's side
            num_to_place = 2
            moves = []
            for i in range(0, num_to_place):
                move = None
                while move is None:
                    # Choose any x location
                    x = random.randint(0, 9)
                    # Choose any y location on enemy side of the board
                    y = random.randint(6, 9)
                    # Set the move if this space is empty
                    if currentState.board[x][y].constr is None and (x, y) not in moves:
                        move = (x, y)
                        # Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr is True
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
        # set global variable playerIndex
        if self.playerIndex is None:
            self.playerIndex = currentState.whoseTurn
        cpy_state = currentState.fastclone()
        self.foods = getConstrList(currentState, None, (FOOD,))
        self.homes = getConstrList(currentState, currentState.whoseTurn, (ANTHILL, TUNNEL,))

        move = self.startBestMoveSearch(cpy_state, cpy_state.whoseTurn)

        return move

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
    # startBestMoveSearch
    # Description: Finds the best move by looking at a search tree
    # and selecting the best node witch contains the a move
    #
    # Parameters:
    #   state - A clone of the current state (GameState)
    #   me - reference to who's turn it is
    ##
    def startBestMoveSearch(self, state, me):
        moves = []
        currScore = self.scoreState(state, me)
        moves = listAllLegalMoves(state)
        thisNode = {"move": None, "state": state, "score": self.scoreState(state, me), "parentNode": None}
        nextStates = []
        for move in moves:
            nextStates.append(self.getNextStateAdversarial(state, move))
        nextNodes = []
        alpha = float("-inf")
        beta = float("inf")
        for i in range(0, len(moves)):
            nextNodes.append(self.TestMethod(moves[i], nextStates[i], 1, me, thisNode, alpha, beta))
        selectMove = Move(END, None, None)
        for node in nextNodes:
            if node["score"] >= currScore:
                selectMove = node["move"]
                currScore = node["score"]
        # if selectMove.moveType == END:
        #    print("End Turn")
        return selectMove

    ##
    # getBestMove
    # Description: Finds the best move by looking at a search tree
    # and selecting the best node witch contains the a move
    #
    # Parameters:
    #   move - a move from a list of legal moves
    #   state - A clone of the current state (GameState)
    #   depth - the current depth of the tree
    #   me - reference to who's turn it is
    #   parent - reference to parent node
    ##
    def getBestMove(self, move, state, depth, me, parent, alpha, beta):
        thisNode = {"move": move, "state": state, "score": self.scoreState(state, me), "parentNode": parent}
        moves = []
        moves = listAllLegalMoves(state)
        if len(moves) == 0: return thisNode
        nextStates = []
        for move in moves:
            nextStates.append(self.getNextStateAdversarial(state, move))
        if depth == self.depthLimit:
            scores = []
            for s in nextStates:
                scores.append(self.scoreState(s, me))
            if thisNode["state"].whoseTurn == self.playerIndex:
                thisNode["score"] = max(scores)
            else:
                thisNode["score"] = min(scores)
        else:
            nextNodes = []
            for i in range(0, len(moves)):
                nextNodes.append(self.getBestMove(moves[i], nextStates[i], depth + 1, me, thisNode, alpha, beta))
            if thisNode["state"].whoseTurn == self.playerIndex:
                nodeListScore = self.scoreNodeList(nextNodes)
                if thisNode["score"] <= nodeListScore:
                    thisNode["score"] = nodeListScore
            else:
                nodeListScore = self.scoreNodeListMin(nextNodes)
                if thisNode["score"] >= nodeListScore:
                    thisNode["score"] = nodeListScore
        return thisNode

    # TODO change name of this function and delete getBestMove
    def TestMethod(self, move, state, depth, me, parent, alpha, beta):
        # Create a new node
        this_node = {"move": move, "state": state, "score": self.scoreState(state, me), "parentNode": parent}
        # If depth limit reach, then just return this node
        if depth == self.depthLimit:
            return this_node
        else:
            moves = listAllLegalMoves(state)  # Get all legal moves
            if len(moves) == 0:
                return this_node  # This should never happen
            # Min max evaluations
            # If this AI's turn, then it is a max evaluation
            # Otherwise it is a min evaluation.
            # Using alpha beta, if beta <= alpha then don't look at any more branches.
            if this_node["state"].whoseTurn == self.playerIndex:
                best = -1000
                for i in range(0, len(moves)):
                    next_state = self.getNextStateAdversarial(state, moves[i])
                    next_node = self.TestMethod(moves[i], next_state, depth + 1, me, this_node, alpha, beta)
                    best = max(best, next_node["score"])
                    alpha = max(alpha, best)
                    if beta <= alpha:  # No need to look at other branches
                        break
                return this_node
            # Min Evaluations
            else:
                worst = 1000
                for i in range(0, len(moves)):
                    next_state = self.getNextStateAdversarial(state, moves[i])
                    next_node = self.TestMethod(moves[i], next_state, depth + 1, me, this_node, alpha, beta)
                    worst = min(worst, next_node["score"])
                    beta = min(beta, worst)
                    if beta <= alpha:  # No need to look at other branches
                        break
                return this_node

    # TODO delete Later
    def scoreNodeList(self, nodes):
        scores = []
        for node in nodes:
            scores.append(node["score"])
        return max(scores)

    # TODO delete later
    def scoreNodeListMin(self, nodes):
        scores = []
        for node in nodes:
            scores.append(node["score"])
        return min(scores)

    ##
    # scoreState
    # Description: scores the advantage of the current state form 1.0 to -1.0,
    # higher numbers advantaging the 'me' player
    #
    # Parameters:
    #   gameState - gameState to analyze
    ##
    def scoreState(self, gameState, me):
        playerFoodGross = gameState.inventories[me].foodCount
        playerFoodScaled = playerFoodGross / 11.0
        score = playerFoodScaled
        workers = getAntList(gameState, me, (WORKER,))

        if score < 1.0:
            if len(workers) < 2: score = score - .1
            for worker in workers:
                if worker.carrying:
                    score = score + .01
                    stepsToHomes = (
                    approxDist(worker.coords, self.homes[0].coords), approxDist(worker.coords, self.homes[1].coords))
                    minSteps = min(stepsToHomes)
                    score = score + .01 / (1.0 + minSteps)
                else:
                    stepsToFoods = (
                    approxDist(worker.coords, self.foods[0].coords), approxDist(worker.coords, self.foods[1].coords), \
                    approxDist(worker.coords, self.foods[2].coords), approxDist(worker.coords, self.foods[3].coords))
                    minSteps = min(stepsToFoods)
                    score = score + .01 / (1.0 + minSteps)

        return score

    ##
    # registerWin
    #
    # This agent doens't learn
    #
    def registerWin(self, hasWon):
        # method templaste, not implemented
        pass

    ##
    # This is an updated method that was written by Jacob Apenes and sent to everyone by Nuxoll
    # We put this in our agent's class to make sure that the updated version is used instead of the one in the
    # AIPlayerUtils class.
    #
    # Thank You Jacob!!!!!
    #
    # getNextStateAdversarial
    #
    # Description: This is the same as getNextState (above) except that it properly
    # updates the hasMoved property on ants and the END move is processed correctly.
    #
    # Parameters:
    #   currentState - A clone of the current state (GameState)
    #   move - The move that the agent would take (Move)
    #
    # Return: A clone of what the state would look like if the move was made
    ##
    def getNextStateAdversarial(self, currentState, move):
        # variables I will need
        nextState = getNextState(currentState, move)
        myInv = getCurrPlayerInventory(nextState)
        myAnts = myInv.ants

        # If an ant is moved update their coordinates and has moved
        if move.moveType == MOVE_ANT:
            # startingCoord = move.coordList[0]
            startingCoord = move.coordList[len(move.coordList) - 1]
            for ant in myAnts:
                if ant.coords == startingCoord:
                    ant.hasMoved = True
        elif move.moveType == END:
            for ant in myAnts:
                ant.hasMoved = False
            nextState.whoseTurn = 1 - currentState.whoseTurn
        return nextState


# TODO possible add more unit test methods
def testMeeseek():
    gameState = GameState.getBasicState()
    gameState.inventories[0].foodCount = 11
    AI = AIPlayer(PLAYER_ONE)
    winstate = AI.scoreState(gameState, 0)
    if winstate != 1:
        print('You have an error in your scoreState, not recording 11 food as victory')
    else:
        print("passed unit test")


testMeeseek()
