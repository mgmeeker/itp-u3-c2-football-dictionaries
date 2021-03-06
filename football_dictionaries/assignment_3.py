from .assignment_1 import players_as_dictionaries  # Thanks @ColemanSWE for sharing your notes. 

def players_by_country_and_position(squads_list):
    list_by_country = {}
    players_as_dicts = players_as_dictionaries(squads_list)


    for player in players_as_dicts:
        position = player['position']
        country = player['country']
        list_by_country.setdefault(country, {})
        list_by_country[country].setdefault(position, [])
        list_by_country[country][position].append(player)
    return list_by_country
    
    