def BaseAgent(object):
    def __init__(n_actions):
        self.n_actions=n_actions
    def update(state):
        self.state=state
        action=self.get_action(state)
        self.perform_action(action)
    def get_action(state):
        pass
    def perform_action(action):
       pass


