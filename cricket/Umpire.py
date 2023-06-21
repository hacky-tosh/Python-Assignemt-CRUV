import random

class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, batsman):
        return random.choice(['out', 'boundary', 'dot'])

    def make_decision(self, decision_type):
        return random.choice([True, False])

    def update_scores(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1
