import math

class MDP:
    # states: [States]
    # actions: [Action]
    # transitions: (State, Action) -> [(Number, State)]
    # utility: (State, Action) -> Number
    def __init__(states, actions, transitions, utility):
        self.states = states
        self.actions = actions
        self.t = transitions
        self.u = utility
    
    def heuristic(self, iterations):
        if iterations == 0:
            return emptyHeuristc(self.states, self.action)

        heuristic = self.heuristic(iterations - 1)

        newHeuristic = emptyHeuristic(self.states, self.actions)
        for s in self.states:
            for a in self.actions:
                value = 0.0
                for (p, s) in self.t(s, a):
                    value += p * maxValue(heuristic[s])

                newHeuristic[s][a] = value

        return newHeuristic
                

def maxValue(d):
    n = -math.inf
    for (k, v) in d:
        n = max(n, v)

    return n


def emptyHeuristic(states, actions):
    policy = dict()

    for s in states:
        d = dict()
        for a in actions:
            d[a] = 0.0
        
        policy[s] = d
    
    return policy