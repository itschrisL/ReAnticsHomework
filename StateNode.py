class StateNode:

    stateNode = [
        {"Data": [
            "currentState",
            "previousMove",  # Move that was taken to get to this state
            "nextMove",  # Next best move
            "nextState",  # State that will be reached from nextMove
            "stateScore",
        ]},
        {"Nodes": [
            "parentNode",
            "subNodes",
        ]}
    ]

    def __init__(self, state, previousState, score, move, depth, parent=None, subNode=None):
        self.nextState = state  # the state that would be reached by taking that move
        self.previousState = previousState
        self.move = move  # the Move that would be taken in the given state from the parent node
        self.score = score  # an evaluation of this state
        self.parentNode = parent
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
