"""
Thomas Kanenaga
CSE 163 AD

This file contains the code to answer all questions relating
 to the second homwork not utilizing pandas.
"""


def species_count(data):
    """
    Takes in the pokemon dataset and returns the number of unique
    pokemon species in the dataset as determined by the different
    names in the dataset.
    """
    unique_pokemon = set()
    for pokemon in data:
        unique_pokemon.add(pokemon["name"])
    return len(unique_pokemon)


def max_level(data):
    """
    This fuction takes in the pokemon data and returns
    the name and level of the highest pokemon as a tuple.
    """
    high_level = 0
    for row in data:
        if row['level'] > high_level:
            high_level = row['level']
            top_level = (row['name'], row['level'])
    return top_level


def filter_range(data, x, y):
    """
    This function takes in the pokemon dataset and two numbers
    (x and y): a lower bound(inclusive) and upper bound (exclusive).
    The function returns a list of the names that fall in between the range.
    """
    pokemon_names = []
    for pokemon in data:
        if pokemon["level"] >= x and pokemon["level"] < y:
            pokemon_names.append(pokemon["name"])
    return pokemon_names


def mean_attack_for_type(data, types):
    """
    This function takes the pokemon dataset and a string
    representing the pokemon type and returns the average
    attack level for all the pokemon in the dataset with
    the given type.
    """
    pokemon_count = 0
    tot_attack = 0
    for pokemon in data:
        if types in pokemon["type"]:
            tot_attack += pokemon["atk"]
            pokemon_count += 1
    if pokemon_count == 0:
        return None
    else:
        return (tot_attack/pokemon_count)


def count_types(data):
    """
    This function takes the pokemon dataset and returns
    a dictionary representing for each pokemon type the
    number of pokemon of that type.
    """
    pokemon_type = {}
    count_pokemon_types = []
    for pokemon in data:
        count_pokemon_types.append(pokemon["type"])
    for pokemon in data:
        if pokemon["type"] not in pokemon_type:
            pokemon_type[pokemon["type"]] = (
                count_pokemon_types.count(pokemon["type"]))
    return pokemon_type


def mean_attack_per_type(data):
    """
    This function takes in the pokemon dataset and returns
    the mean of the attack level for each type found in the
    data set.
    """
    mean_dict = {}
    for pokemon in data:
        if pokemon["type"] not in mean_dict:
            mean_dict[pokemon["type"]] = mean_attack_for_type(
                data, pokemon["type"])
    return mean_dict
