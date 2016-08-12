import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import operator
from collections import defaultdict

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env, alphaBetaGamma=(0.8, 0.5, 0.1)):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint

        # Initialize any additional variables here
        self.penalty = 0
        self.reward = 0

        # learning rate alpha
        self.alpha = alphaBetaGamma[0]

        # discount factor gamma
        self.gamma = alphaBetaGamma[1]

        # exploration rate epsilon
        self.epsilon = alphaBetaGamma[2]
        print "Alpha {}, Gamma {}, Epsilon {}".format(self.alpha, self.gamma, self.epsilon)

        # initial Q values 1 for each action
        self.Q = defaultdict(self.getDefaultQvalues)

        self.totalPenaltiesSuccess = []
        self.totalRewardsSuccess = []
        self.totalStepsSuccess = []
        self.totalPenaltiesFailure = []
        self.totalRewardsFailure = []
        self.totalStepsFailure = []

    def getDefaultQvalues(self):
        Q = {}
        for action in self.env.getActions():
            Q[action] = 1
        return Q


    def reset(self, destination=None):
        self.planner.route_to(destination)
        # Prepare for a new trip; reset any variables here, if required
        self.penalty = 0
        self.reward = 0

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # Update state
        self.state = (self.next_waypoint, inputs['light'], inputs['oncoming'], inputs['left'])

        # Select action according to your policy
        action = self.chooseAction()

        # Execute action and get reward
        reward = self.env.act(self, action)
        if reward < 0:
            self.penalty += 1

        # Learn policy based on state, action, reward
        self.learn(t, action, reward)
        self.reward += reward

        # print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]
        if self.planner.next_waypoint() == None:
            self.totalRewardsSuccess.append(self.reward)
            self.totalPenaltiesSuccess.append(self.penalty)
            self.totalStepsSuccess.append(t + 1)
        elif deadline == 0:
            self.totalRewardsFailure.append(self.reward)
            self.totalPenaltiesFailure.append(self.penalty)
            self.totalStepsFailure.append(t + 1)

    def learn(self, t, action, reward):
        """
        Q Learning algorithm.
        :param t: state
        :param action: action
        :param reward: reward
        :return:
        """
        learningRate = 1.0 / (t + 1) ** self.alpha

        newWaypoint = self.planner.next_waypoint()
        newInputs = self.env.sense(self)
        newState = (newWaypoint, newInputs['light'], newInputs['oncoming'], newInputs['left'])
        newAction = self.chooseAction(newState)
        newQ = reward + self.gamma * newAction[1]

        currentQ = self.Q[self.state][action]
        self.Q[self.state][action] = (1 - learningRate) * currentQ + learningRate * newQ


    def chooseAction(self, state=None):
        """
        Chooses best action based on the state.
        :param state: either use current, or provided if state is not none
        :return: best action to perform, based on the state
        """
        if (state):
            actions = self.Q[state]
            return max(actions.iteritems(), key=operator.itemgetter(1))

        bestAction = max(self.Q[self.state].iteritems(), key=operator.itemgetter(1))[0]
        if random.random() < self.epsilon:
            random_actions = [action for action in self.env.valid_actions if action != bestAction]
            return random.choice(random_actions)

        return bestAction


def run():
    """Run the agent for a finite number of trials."""

    def runWithParams(alpha, gamma, epsilon):
        # Set up environment and agent
        e = Environment()  # create environment (also adds some dummy traffic)
        a = e.create_agent(LearningAgent, (alpha, gamma, epsilon))  # create agent
        e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
        # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

        # Now simulate it
        sim = Simulator(e, update_delay=0.000001, display=False)  # create simulator (uses pygame when display=True, if available)
        # NOTE: To speed up simulation, reduce update_delay and/or set display=False
        sim.run(n_trials=100)  # run for a specified number of trials
        # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line

    alphas = [0.8]
    gammas = [0.1]
    epsilons = [0.005]

    # A lot of work :)
    for alpha in alphas:
        for gamma in gammas:
            for epsilon in epsilons:
                runWithParams(alpha, gamma, epsilon)

if __name__ == '__main__':
    run()
