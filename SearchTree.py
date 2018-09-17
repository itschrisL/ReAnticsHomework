
class SearchTree:

    root = [{"Root Node": []}]

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
        self.size = 0
        self.depth = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def insert(self, node, currentState):
        if self.top == None:
            self.top = node

    def remove(self, node, currentState):
        if self.top == None:
            pass

    def find(self, node, currentState):
        if self.top == None:
            pass
