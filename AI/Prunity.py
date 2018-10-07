import sys
import unittest

sys.path.append("..")  # so other modules can be found in parent dir
from Player import *
from GameState import *
from AIPlayerUtils import *
from SearchTree import SearchTree
from StateNode import StateNode


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
        super(AIPlayer, self).__init__(inputPlayerId, "Prunity")
        self.searchTree = SearchTree()
        self.searchTree.depthLimit = 1
        self.myTunnel = None
        self.myFood = None
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
        if self.playerIndex == None:
            self.playerIndex = me

        foods = getConstrList(currentState, None, (FOOD,))

        # Find Food and Tunnel of agent
        if self.myTunnel is None:
            self.myTunnel = getConstrList(currentState, me, (TUNNEL,))[0]
        if self.myFood == None:
            closest = 1000
            for food in foods:
                dist = approxDist(self.myTunnel.coords, food.coords)
                if (dist < closest):
                    self.myFood = food
                    closest = dist

        # Start of the recursive method
        self.searchTree.top = StateNode(currentState, None, None, None, 0)
        self.searchTree.top.subNodes = self.RecursiveFindMove(currentState, 0)
        # Find best move
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

    #
    # Recursive method to find the best move with MinMax
    #
    def RecursiveFindMoveMinMax(self, currentState, currentDepth):
        if currentDepth <= self.searchTree.depthLimit:
            nodes = []
            states = []  # List of next states being generated by each move
            node = StateNode(currentState, None, 0, None, currentDepth, None, None)
            moves = listAllLegalMoves(currentState)  # List of all legal moves from that state
            for move in moves:
                states.append(getNextStateAdversarial(currentState, move))
            # Look at the first 100 states
            if len(states) < 100:
                x = len(states)
            else:
                x = 100
            for i in range(0, x):
                newNode = StateNode(states[i], currentState, 0, moves[i], currentDepth, node, None)
                newNode.score = self.calculateStateScore(states[i])
                nodesToCalculate = self.RecursiveFindMoveMinMax(states[i], currentDepth + 1)
                if nodesToCalculate is not None:
                    newNode.subNodes = nodesToCalculate
                    node.score = self.BestNodeInList(nodesToCalculate)
                nodes.append(newNode)
            return nodes
        else:
            return None

    #
    # Recursive search method to find best move
    # if the currentDepth is greater then the depthLimit return None
    #
    def RecursiveFindMove(self, GameState, currentDepth):
        if currentDepth <= self.searchTree.depthLimit:
            nodes = []
            states = []  # List of next states being generated by each move
            node = StateNode(GameState, None, 0, None, currentDepth, None, None)
            moves = listAllLegalMoves(GameState)  # List of all legal moves from that state
            for move in moves:
                states.append(getNextState(GameState, move))
            if len(states) < 10:
                x = len(states)
            else:
                x = 10
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

    def maxNodes(self, currentState):
        bestNode = StateNode(currentState, None, None, None, None)
        return bestNode

    ##
    #
    #
    def BestMaxNode(self, nodes):
        if nodes is not None:
            if len(nodes) > 0:
                best = -100
                for node in nodes:
                    if node.score != None:
                        if node.score > best:
                            best = node.score
                return best
            else:
                return 0

        return 0

    ##
    # Best node for Min
    #
    def BestMinNode(self, nodes):
        if nodes is not None:
            if len(nodes) > 0:
                best = 100
                for node in nodes:
                    if node.score != None:
                        if node.score < best:
                            best = node.score
                return best
            else:
                return 0

        return 0

    # Finds the best Node in the List of Nodes
    # Based on score
    def BestNodeInList(self, nodes):
        if nodes is not None:
            if len(nodes) > 0:
                best = -100
                for node in nodes:
                    if node.score != None:
                        if node.score > best:
                            best = node.score
                return best
            else:
                return 0

        return 0

    # Method to call to evaluate a GameState
    # Calls helper methods to help it with this task
    def calculateStateScore(self, currentState):
        rtrnNumber = self.hasPlaerWon(currentState)
        if self.hasPlaerWon(currentState) == 10 or self.hasPlaerWon(currentState) == -10:
            return rtrnNumber
        else:
            rtrnNumber = self.workerAnts(currentState) + self.numOfFood(currentState) + self.numOfAnts(currentState) + \
                         self.hasPlaerWon(currentState) + self.myQueenThreat(currentState) + \
                         self.DroneTunnelAttack(currentState)
            if currentState.whoseTurn != self.playerIndex:
                rtrnNumber = (rtrnNumber) * (-1)
        return rtrnNumber

    ##
    # If there is enemy ants close to my queen
    #
    def myQueenThreat(self, currentState):
        myID = currentState.whoseTurn
        enemyID = 1 - myID

        myInv = currentState.inventories[myID]
        enemyInv = currentState.inventories[enemyID]

        antHillCords = getConstrList(currentState, currentState.whoseTurn, (ANTHILL,))[0]
        tunnelCords = getConstrList(currentState, currentState.whoseTurn, (TUNNEL,))[0]
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
        if antHillCords.coords == queenCords or tunnelCords.coords == queenCords:
            rtrnNumber = rtrnNumber + -1
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
        return rtrnNumber

    # Checks if the and player has won and updates evaluation score
    #
    def hasPlaerWon(self, currentState):
        if getWinner(currentState) is None:
            return 0.0
        elif getWinner(currentState) == 1:
            return 10.0
        elif getWinner(currentState) == 0:
            return -10.0
        else:
            return 0

    # If Any soldier is getting closer to the the enemy tunnel
    # Update Score Positively
    def DroneTunnelAttack(self, currentState):
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
            return self.enemyQueenThreat(currentState)
        return 0

    #
    #
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

    #
    #
    def numOfAnts(self, currentState):
        enemyWorkers = getAntList(currentState, 1 - currentState.whoseTurn, (WORKER,))
        enemySoilders = getAntList(currentState, 1 - currentState.whoseTurn, (R_SOLDIER, DRONE, SOLDIER,))

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

        if len(enemySoilders) == 0:
            rtrnNumber = rtrnNumber + 1
        else:
            rtrnNumber = rtrnNumber + (-0.8 * len(enemySoilders))
        return rtrnNumber

    ##
    # numOfFood
    #
    # Calculates the amount of food that the human has
    def numOfFood(self, currentState):
        enemyFood = getEnemyInv(self, currentState).foodCount
        myInv = currentState.inventories[currentState.whoseTurn]

        if myInv.foodCount == 0:
            rtrnNumber = -0.3
        else:
            rtrnNumber = myInv.foodCount * 0.5
        return rtrnNumber

    # Calculates the distance from worker to a food and returns a better score if the worker is getting closer
    # to the food or is caring food back to the tunnel
    #
    def workerAnts(self, currentState):
        rtrnNumber = 0
        foods = getConstrList(currentState, None, (FOOD,))
        if len(foods) != 0:
            me = currentState.whoseTurn
            foods = getConstrList(currentState, None, (FOOD,))

            # Get of Tunnel
            self.myTunnel = getConstrList(currentState, me, (TUNNEL,))[0]
            # Find Closest Food
            closest = 1000
            for food in foods:
                dist = approxDist(self.myTunnel.coords, food.coords)
                if dist < closest:
                    myFood = food
                    closest = dist
            myTunnel = self.myTunnel
            myWorkers = getAntList(currentState, currentState.whoseTurn, (WORKER,))

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
                rtrnNumber = -1
        return rtrnNumber


# UNIT TESTS

# Get basic State
state = GameState.getBasicState()

temp = AIPlayer.hasPlaerWon(AIPlayer, state)
test = getWinner(state)
if temp == 10 or temp == -10:
    print("hasPlayerWon Unit Test: True")
else:
    print("hasPlayerWon Unit Test: False")
# Generate basic states
state1 = GameState.getBasicState()
state2 = GameState.getBasicState()
state3 = GameState.getBasicState()
# Add Ants
state1.inventories[0].ants.append(Ant((1, 1), R_SOLDIER, 0))
state1.inventories[0].ants.append(Ant((1, 1), WORKER, 0))
state2.inventories[0].ants.append(Ant((1, 1), WORKER, 0))
state2.inventories[0].ants.append(Ant((2, 2), SOLDIER, 0))
state2.inventories[0].ants.append(Ant((1, 1), R_SOLDIER, 0))
state3.inventories[0].ants.append(Ant((1, 1), WORKER, 0))

state1.inventories[1].ants.append(Ant((1, 1), R_SOLDIER, 1))
state1.inventories[1].ants.append(Ant((1, 1), WORKER, 1))
state2.inventories[1].ants.append(Ant((1, 1), WORKER, 1))
state2.inventories[1].ants.append(Ant((2, 2), SOLDIER, 1))
state2.inventories[1].ants.append(Ant((1, 1), R_SOLDIER, 1))
state3.inventories[1].ants.append(Ant((1, 1), WORKER, 1))
# Add Food
state1.inventories[0].foodCount = 0
state2.inventories[0].foodCount = 5
state3.inventories[0].foodCount = 2

# Test method numOfFood
numberOfFood1 = AIPlayer.numOfFood(AIPlayer, state3)
numberOfFood2 = AIPlayer.numOfFood(AIPlayer, state1)
numberOfFood3 = AIPlayer.numOfFood(AIPlayer, state2)
if numberOfFood1 == 1:
    print("numOfFood Unit Test: True")
else:
    print("numOfFood Unit Test: False")
if numberOfFood2 == -0.3:
    print("numOfFood Unit Test: True")
else:
    print("numOfFood Unit Test: False")

if numberOfFood3 == 2.5:
    print("numOfFood Unit Test: True")
else:
    print("numOfFood Unit Test: False")

# Test Method numOfAnts
numAnts1 = AIPlayer.numOfAnts(AIPlayer, state1)
numAnts2 = AIPlayer.numOfAnts(AIPlayer, state2)
numAnts3 = AIPlayer.numOfAnts(AIPlayer, state3)
if numAnts1 == 0.09999999999999998:
    print("numOfAnts Unit Test: True")
else:
    print("numOfAnts Unit Test: False")
if numAnts2 == -1.2000000000000002:
    print("numOfAnts Unit Test: True")
else:
    print("numOfAnts Unit Test: False")
if numAnts3 != 0.0:
    print("numOfAnts Unit Test: True")
else:
    print("numOfAnts Unit Test: False")

# Test MyQueenThreat
queenThr1 = AIPlayer.myQueenThreat(AIPlayer, state1)
queenThr2 = AIPlayer.myQueenThreat(AIPlayer, state2)
queenThr3 = AIPlayer.myQueenThreat(AIPlayer, state3)
if queenThr1 == -1.25:
    print("myQueenThreat Unit Test: True")
else:
    print("myQueenThreat Unit Test: False")
if queenThr2 == -1.25:
    print("myQueenThreat Unit Test: True")
else:
    print("myQueenThreat Unit Test: False")
if queenThr3 == -1:
    print("myQueenThreat Unit Test: True")
else:
    print("myQueenThreat Unit Test: False")

# Test Best Node in List
node1 = StateNode(state1, None, 5, None, 0, None, None)
node2 = StateNode(state1, None, 1, None, 0, None, None)
node3 = StateNode(state1, None, -3, None, 0, None, None)
node4 = StateNode(state1, None, None, None, 0, None, None)
nodes = {node1, node2, node3, node4}
sum = AIPlayer.BestNodeInList(AIPlayer, nodes)
if sum == 5:
    print("BestNodeInList Unit Test: True")
else:
    print("BestNodeInList Unit Test: False")

# Test method workerAnts
worker1 = AIPlayer.workerAnts(AIPlayer, state1)
worker2 = AIPlayer.workerAnts(AIPlayer, state1)
worker3 = AIPlayer.workerAnts(AIPlayer, state1)
print("\n\nCould not find way to add food to board for testing  \n"
      "So all methods return false because there is no food on board")
if worker1 == -0.5:
    print("workerAnts Unit Test: True")
else:
    print("workerAnts Unit Test: False")
if worker1 == -0.5:
    print("workerAnts Unit Test: True")
else:
    print("workerAnts Unit Test: False")
if worker1 == -0.5:
    print("workerAnts Unit Test: True")
else:
    print("workerAnts Unit Test: False")


class SearchTree:

    def __init__(self):
        self.nodes = []
        self.top = None
        self.size = 0
        self.depth = 0
        self.depthLimit = 1

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    ##
    # Insert
    # Method to insert and new node to a parent's subnode list.
    #
    # Input:
    #   - parent - Inserted node's parent
    #   - node - Node to be inserted
    #   - currentState - Current state of board.
    def insert(self, parent, node):
        if self.top is None:
            self.top = node
        else:
            if not parent.subnodes.contains(node):
                parent.subnodes.append(node)
                self.size += 1

    # Not implemented
    def remove(self, node, currentState):
        if self.top == None:
            pass

    def find(self, node, GameState):
        if self.top == None:
            return None
        else:
            for n in node.subNodes:
                if n is node:
                    return n
                else:
                    self.find(self, node, GameState)
        return None  # Meaning node not in tree


class StateNode:

    def __init__(self, state, previousState, score, move, depth, parent=None, subNode=None):
        self.nextState = state  # the state that would be reached by taking that move
        self.previousState = previousState
        self.move = move  # the Move that would be taken in the given state from the parent node
        self.score = score  # an evaluation of this state
        self.parentNode = parent
        self.subNodes = []
        self.subNodes = subNode
        self.depth = depth

    def HasSubNode(self):
        print("Has Sub Node: " + str((len(self.subNodes) <= 0)))
        return len(self.subNodes) <= 0

    def IsRoot(self):
        print("Is Root: " + str(not self.parentNode))
        return not self.parentNode

    def IsLeaf(self):
        print("Is Leaf: " + str(len(self.subNodes) <= 0))
        return len(self.subNodes) <= 0

    def ReplaceNodeData(self, state, previousState, score, move, parent=None, subNode=None):
        self.nextState = state  # the state that would be reached by taking that move
        self.previousState = previousState
        self.move = move  # the Move that would be taken in the given state from the parent node
        self.score = score  # an evaluation of this state
        self.parentNode = parent
        self.subNodes = subNode
        for node in subNode:
            node.parent = self

    def AddSubnode(self, node):
        nodes = self.subNodes
        nodes.append(node)
