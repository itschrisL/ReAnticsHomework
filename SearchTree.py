
class SearchTree:

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

    def __init__(self):
        self.nodes = []
        self.top = None

    def insert(self, node, currentState):
        if self.top == None:
            self.top = node

    def remove(self, node, currentState):
        if self.top == None:
            pass

    def find(self, node, currentState):
        if self.top == None:
            pass
