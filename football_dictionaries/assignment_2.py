from collections import OrderedDict


def players_by_position(squads_list):

    player_dictionary = {}

    player_keys_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country',
                        'year']

    for player in squads_list:
        single_player_dictionary = OrderedDict(sorted(zip(player_keys_list, player), key=lambda tup: tup[0]))
        player_dictionary.setdefault(single_player_dictionary['position'], []).append(single_player_dictionary)

    return player_dictionary
