import constants
import copy

if __name__ == "__main__":
    players = copy.deepcopy(constants.PLAYERS)
    teams = copy.deepcopy(constants.TEAMS)

    def clean_data():
        for player in players:
            # first split the string into 2 combined string
            player['height'] = player['height'].split()
            # then pick the first string and cast it into integers
            player['height'] = int(player['height'][0])

            # if the experience key contains "YES" string, then change it into True boolean value
            if player['experience'] == 'YES':
                player['experience'] = True
            else:
                player['experience'] = False

        return players

    def balance_teams(players):
        panthers = []
        bandits = []
        warriors = []
