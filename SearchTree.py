
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
    def insert(self, parent, node, currentState):
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

    # Not implemented
    def find(self, node, currentState):
        if self.top == None:
            return None
        else:
            for n in node.subNodes:
                if n is node:
                    return n
                else:
                    self.find(self, node, currentState)
        return None  # Meaning node not in tree
