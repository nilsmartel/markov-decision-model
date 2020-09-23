import math

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

class MDP:
    # states: [States]
    # actions: [Action]
    # transitions: (State, Action) -> [(Number, State)]
    # reward: (State, Action, State') -> Number
    def __init__(self, states, actions, transitions, reward, falloff = 1.0):
        self.states = states
        self.actions = actions
        self.t = transitions
        self.reward = reward
        self.falloff = falloff


    def heuristic(self, iterations):
        if iterations == 0:
            return emptyHeuristic(self.states, self.actions)

        heuristic = self.heuristic(iterations - 1)

        newHeuristic = emptyHeuristic(self.states, self.actions)

        for s in self.states:
            for a in self.actions:
                value = 0.0
                for (p, sn) in self.t(s, a):
                    value += p* (self.reward(s, a, sn) + self.falloff*maxValue(heuristic[sn]))

                newHeuristic[s][a] = value

        return newHeuristic
