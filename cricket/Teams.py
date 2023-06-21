class Teams:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
        self.batting_order = []
        self.score = 0
        self.wickets = 0

    def add_player(self, player):
        self.players.append(player)

    def select_captain(self):
        captain_name = input(f"\nSelect the captain for Team {self.name}: ")
        for player in self.players:
            if player.name == captain_name:
                self.captain = player
                break
        else:
            print(f"No player found with the name {captain_name} in team {self.name}.")

    def set_batting_order(self):
        print(f"\nEnter the batting order for {self.name}:")
        for i in range(len(self.players)):
            player_name = input(f"Player {i+1}: ")
            for player in self.players:
                if player.name == player_name:
                    self.batting_order.append(player)
                    break
            else:
                print(f"No player found with the name {player_name} in team {self.name}")

    def update_score(self, runs):
        self.score += runs

    def update_wickets(self):
        self.wickets += 1
