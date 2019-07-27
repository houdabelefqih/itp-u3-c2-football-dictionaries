from collections import OrderedDict


def players_as_dictionaries(squads_list):
    
    player_keys_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    result_list = []

    for player in squads_list:
        result_list.append(OrderedDict(sorted(zip(player_keys_list, player), key=lambda tup: tup[0])))

    return result_list
