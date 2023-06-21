from cricket.Player import Player
from cricket.Teams import Teams
from cricket.Field import Field
from cricket.Match import Match
from cricket.Commentator import Commentator


def main():
        print("-------------------------------------")
        print("Welcome to Advance Cricket Tournament")
        print("-------------------------------------")

        # Creating players for the cricket tournament 
        player1_name = input("\nEnter name of player 1 : ")
        player1 = Player(player1_name, 0.2, 0.8, 0.99, 0.8, 0.9)

        player2_name = input("\nEnter name of player 2 : ")
        player2 = Player(player2_name, 0.3, 0.7, 0.95, 0.7, 0.8)

        player3_name = input("\nEnter name of player 3 : ")
        player3 = Player(player3_name, 0.15, 0.85, 0.98, 0.85, 0.95)

        player4_name = input("\nEnter name of player 4 : ")
        player4 = Player(player4_name, 0.25, 0.75, 0.97, 0.75, 0.85)

        # Creating teams
        team1_name = input("\nEnter name of team 1 : ")
        team1 = Teams(team1_name)
        # Adding players to team 1
        team1.add_player(player1)
        team1.add_player(player2)

        # Adding players to team 2
        team2_name = input("\nEnter name of team 2 : ")
        team2 = Teams(team2_name)
        team2.add_player(player3)
        team2.add_player(player4)

        # Creating field
        field_size = input("\nEnter field size: ")
        fan_ratio = input("\nEnter fan ratio: ")
        pitch_conditions = input("\nEnter pitch conditions: ")
        home_advantage = input("\nEnter home advantage: ")
        field = Field(field_size, fan_ratio, pitch_conditions, home_advantage)

        # Creating the match
        match = Match(team1, team2, field)

        # Starting the match
        match.start_match()



if __name__ == "__main__":
    main()
