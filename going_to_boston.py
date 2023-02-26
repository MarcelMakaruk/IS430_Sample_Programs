"""
Simulate a 2-player and 3-die game of Going to Boston with a user-chosen number of rounds and number of players.
"""

from random import randint
import string

MINIMUM_NUMBER_OF_ROUNDS = 0
MAXIMUM_NUMBER_OF_ROUNDS = 1000
MINIMUM_NUMBER_OF_PLAYERS = 2
MAXIMUM_NUMBER_OF_PLAYERS = 26


def main():
    print('Welcome to Going to Boston Pro Edition.\n')
    rounds_to_play = get_number_of_rounds()
    names_of_players = generate_player_names()
    if rounds_to_play == 0:
        print('No rounds were requested.')
    else:
        dict_with_scores = {}
        for i in range(len(names_of_players)):
            dict_with_scores[names_of_players[i]] = 0
        for i in range(1, rounds_to_play + 1):
            round_scores = play_round(i, names_of_players)
            if len(round_scores) > 1:
                pass
            else:
                for j in range(len(round_scores)):
                    if round_scores[j] in dict_with_scores:
                        dict_with_scores[round_scores[j]] += 1
    print_game_results(dict_with_scores)


def get_number_of_rounds():
    valid_value = False
    rounds_as_string = get_rounds_as_string()
    while rounds_as_string != '' and not valid_value:
        try:
            rounds = int(rounds_as_string)
            if MINIMUM_NUMBER_OF_ROUNDS <= rounds <= MAXIMUM_NUMBER_OF_ROUNDS:
                valid_value = True
            else:
                print(f'A valid value has to be greater or equal than 0 and less or equal than 1000. You entered {rounds}.')
                rounds_as_string = get_rounds_as_string()
        except ValueError:
            print(f'An integer was expected. You entered {rounds_as_string}.')
            rounds_as_string = get_rounds_as_string()

    if rounds_as_string == '':
        rounds = 0
    return rounds


def get_rounds_as_string():
    rounds_as_string = input('Please enter the number of rounds to be played (<ENTER> to stop): ')
    return rounds_as_string


def get_number_of_players():
    value_valid = False
    players_as_string = get_players_as_string()
    while players_as_string != '' and not value_valid:
        try:
            players = int(players_as_string)
            if MINIMUM_NUMBER_OF_PLAYERS <= players <= MAXIMUM_NUMBER_OF_PLAYERS:
                value_valid = True
            else:
                print(f'A valid value has to be greater or equal than 2 and less or equal than 26. You entered {players}.')
                players_as_string = get_players_as_string()
        except ValueError:
            print(f'An integer was expected. You entered {players_as_string}.')
            players_as_string = get_players_as_string()
    return players


def get_players_as_string():
    players_as_string = input('Please enter the number of players participating: ')
    return players_as_string


def generate_player_names():
    number_of_players = get_number_of_players()
    list_of_players = []
    for i in range(0, number_of_players):
        list_of_players.append(string.ascii_uppercase[i])
    return list_of_players


def play_round(round_number, player_names):
    print(f'\nPlaying Round {round_number}: ')
    scores_dict_turn = {}
    for i in range(len(player_names)):
        scores_sum = three_rolls(player_names[i])
        scores_dict_turn[player_names[i]] = scores_sum
    list_of_highest_scores_keys = [key for key, value in scores_dict_turn.items() if value == max(scores_dict_turn.values())]
    if len(list_of_highest_scores_keys) > 1:
        print('There was no winner for this round.')
    elif len(list_of_highest_scores_keys) == 1:
        print(f'Player {" ".join(list_of_highest_scores_keys)} wins the round!')
    return list_of_highest_scores_keys


def three_rolls(name_player):
    scores = []
    print(f'Player {name_player}\'s turn...')
    for i in range(1, 3 + 1):
        print(f'Roll number {i}:')
        turn_score = play_turn(name_player)
        scores.append(turn_score)
        print(f'From the roll number {i} player {name_player} chooses {turn_score}')
    scores_sum = sum(scores)
    print(f'===>The sum of scores for player {name_player} is {scores_sum}\n')
    return scores_sum


def play_turn(player_name):
    rolls = roll_dice(3)
    print(f'Player {player_name} rolls {rolls}.')
    choice = choose_highest_roll(rolls)
    return choice


def roll_dice(number_of_dice):
    rolls = []
    for i in range(number_of_dice):
        rolls.append(roll_die())
    return rolls


def roll_die():
    return randint(1, 6)


def choose_highest_roll(these_rolls):
    highest_roll = max(these_rolls)
    return highest_roll


def print_game_results(scores_round):
    print('\nGame Results:')
    for key, value in scores_round.items():
        if value == 1:
            print(f'Player {key} has won {value} round')
        else:
            print(f'Player {key} has won {value} rounds')

    winners_list = [key for key, value in scores_round.items() if value == max(scores_round.values())]
    if len(winners_list) == 1:
        print(f'Player {" ".join(winners_list)} wins the game!')
    else:
        for i in range(len(winners_list)):
            print(f'Player {" ".join(winners_list[i])} has tied for the win.')


main()
