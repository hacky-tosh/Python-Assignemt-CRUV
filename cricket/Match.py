import random
from cricket.Commentator import Commentator
from cricket.Umpire import Umpire



class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.Commentator = Commentator()
        self.umpire = Umpire()

    def start_match(self):

        self.team1.select_captain()
        self.team2.select_captain()

        self.team1.set_batting_order()
        self.team2.set_batting_order()

        print("\n*******************")
        print("Starting the Match")
        print("*******************")

        # innings for Team 1
        team1_score = self.innings(self.team1)
        print(f"\nTeam {self.team1.name} Final Score: {team1_score}/{self.team1.wickets}")

        # innings for Team 2
        team2_score = self.innings(self.team2)
        print(f"\nTeam {self.team2.name} Final Score: {team2_score}/{self.team2.wickets}")

         # choosing winner
        if team1_score > team2_score:
            print(f"\nTeam {self.team1.name} wins!")
        elif team2_score > team1_score:
            print(f"\nTeam {self.team2.name} wins!")
        else:
            print("\nMatch Tied!")
            

    def innings(self, team):
        score = 0
        wickets = 0
        overs = 0

        for player in team.batting_order:
            for over in range(self.field.overs_limit):
                overs += 1
                for ball in range(6):
                    decision_type = random.choice(['LBW', 'Catch', 'No Ball', 'Wide Ball'])
                    decision = self.umpire.make_decision(decision_type)

                    if decision_type == 'LBW' and decision:
                        wickets += 1
                        print(f"{team.name} - Wicket! {player.name} is out (LBW).\n")
                        self.umpire.update_wickets()
                        self.Commentator.provide_commentary(score, wickets, overs)
                        if wickets == self.field.wickets_limit:
                            return score
                        break
                    elif decision_type == 'Catch' and decision:
                        wickets += 1
                        print(f"{team.name} - Wicket! {player.name} is catch out.\n")
                        self.umpire.update_wickets()
                        self.Commentator.provide_commentary(score, wickets, overs)
                        if wickets == self.field.wickets_limit:
                            return score
                        break
                    elif decision_type == 'No Ball' and decision:
                        runs = random.randint(0, 6)
                        score += runs
                        print(f"{team.name} - No Ball! {player.name} scored {runs} runs.\n")
                        self.umpire.update_scores(runs)
                    elif decision_type == 'Wide Ball' and decision:
                        runs = random.randint(0, 6)
                        score += runs
                        print(f"{team.name} - Wide Ball! {player.name} scored {runs} runs.\n")
                        self.umpire.update_scores(runs)
                    else:
                        runs = random.randint(0, 6)
                        score += runs
                        print(f"{team.name} - {runs} runs scored by {player.name}.\n")
                        self.umpire.update_scores(runs)

                    self.umpire.update_overs()
                    self.Commentator.provide_commentary(score, wickets, f"{str(overs-1)}.{str(ball+1)}")
                
                if wickets == self.field.wickets_limit:
                    return score

        return score