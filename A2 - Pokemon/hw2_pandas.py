"""
Thomas Kanenaga
CSE 163 AD

This file contains the code to answer all questions relating
 to the second homwork utilizing pandas.
"""


def species_count(data):
    """
    Using pandas, this funtion takes in the pokemon dataset and
    returns the number of unique pokemon species in the
    as determined by the different names in the dataset.
    """
    names = data["name"].unique()
    return len(names)


def max_level(data):
    """
    Takes a pokemon dataset and returns a 2-element tuple of the
    (name, level) of the pokemon with the highest level in the dataset.
    """
    the_id = data.loc[data["level"].idxmax()]
    return the_id["name"], the_id["level"]


def filter_range(data, x, y):
    """
    using pandas package this, takes in the pokemon dataset and two
    numbers(x and y): a lower bound(inclusive) and upper bound (exclusive).
    The function returns a list of the names that fall in between the range.
    """
    lower_bound = data["level"] >= x
    upper_bound = data["level"] < y
    range_level = data[lower_bound & upper_bound]
    pokemon_names = range_level["name"]
    return list(pokemon_names)


def mean_attack_for_type(data, types):
    """
    Using pandas, this takes the pokemon dataset and
    a string representing the pokemon type and returns
    the average attack level for all the pokemon in the dataset with
    the given type.
    """
    pokemon_type = data["type"] == types
    pokemon_type_data = data[pokemon_type]
    if len(pokemon_type_data) == 0:
        return None
    mean_of_type = pokemon_type_data["atk"].mean()
    return mean_of_type


def count_types(data):
    """
    Using pandas, this code takes the pokemon dataset
    and returns a dictionary representing for each pokemon
    type the number of pokemon of that type.
    """
    pokemon_type_count = data["type"].value_counts()
    return dict(pokemon_type_count)


def mean_attack_per_type(data):
    """
    using pandas, this function takes in the pokemon dataset and returns
    the mean of the attack level for each type found in the
    data set.
    """
    mean_attack = data.groupby("type")["atk"].mean()
    return dict(mean_attack)
