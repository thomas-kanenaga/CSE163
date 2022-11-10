"""
Thomas Kanenaga
CSE 163 AD

This file contains the code to test the panda and
functions witten to solve the second Homework.
"""
import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"
THOMAS_TEST_FILE = "/home/thomas_test.csv"


def test_species_count(spec_test_df, spec_test_data,
                       thomas_test_df, thomas_test_data):
    """
    This function tests the method "species count"
    in both pandas and function form.
    """
    assert_equals(3, hw2_manual.species_count(spec_test_data))
    assert_equals(3, hw2_pandas.species_count(spec_test_df))
    assert_equals(5, hw2_manual.species_count(thomas_test_data))
    assert_equals(5, hw2_pandas.species_count(thomas_test_df))


def test_max_level(spec_test_df, spec_test_data,
                   thomas_test_df, thomas_test_data):
    """
    This function tests the method max_level.
    """
    assert_equals(('Lapras', 72), hw2_manual.max_level(spec_test_data))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(spec_test_df))
    assert_equals(('Ali', 169), hw2_manual.max_level(thomas_test_data))
    assert_equals(('Ali', 169), hw2_pandas.max_level(thomas_test_df))


def test_filter_range(spec_test_df, spec_test_data,
                      thomas_test_df, thomas_test_data):
    """
    This function tests the method filter_range.
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(spec_test_data, 35, 68))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(spec_test_df, 35, 68))
    assert_equals(["Thomas", "Thomas", "Noah", "Cole"],
                  hw2_manual.filter_range(thomas_test_data, 12, 68))
    assert_equals(["Thomas", "Thomas", "Noah", "Cole"],
                  hw2_pandas.filter_range(thomas_test_df, 12, 68))


def test_mean_attack_for_type(spec_test_df, spec_test_data,
                              thomas_test_df, thomas_test_data):
    """
    This function tests the method mean_attack_for_type.
    """
    assert_equals(47.5,
                  hw2_manual.mean_attack_for_type(spec_test_data, "fire"))
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(spec_test_df, "fire"))
    assert_equals(129.333333,
                  hw2_manual.mean_attack_for_type(thomas_test_data, "water"))
    assert_equals(129.333333,
                  hw2_pandas.mean_attack_for_type(thomas_test_df, "water"))


def test_count_types(spec_test_df, spec_test_data,
                     thomas_test_df, thomas_test_data):
    """
    This function tests the method count_types.
    """
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.count_types(spec_test_data))
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.count_types(spec_test_df))
    assert_equals({'fire': 2, 'water': 3, 'electric': 1},
                  hw2_manual.count_types(thomas_test_data))
    assert_equals({'fire': 2, 'water': 3, 'electric': 1},
                  hw2_pandas.count_types(thomas_test_df))


def test_mean_attack_per_type(spec_test_df, spec_test_data,
                              thomas_test_df, thomas_test_data):
    """
    This tests each of the two mean_attack_per_type functions.
    """
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(spec_test_data))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(spec_test_df))
    assert_equals({'fire': 47.5, 'water': 129.333, 'electric': 107.0},
                  hw2_manual.mean_attack_per_type(thomas_test_data))
    assert_equals({'fire': 47.5, 'water': 129.333, 'electric': 107.0},
                  hw2_pandas.mean_attack_per_type(thomas_test_df))


def main():
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)  # a DataFrame
    spec_test_data = parse(SPEC_TEST_FILE)      # a list of dictionaries
    # Feel free to use these datasets in your tests!
    thomas_test_df = pd.read_csv(THOMAS_TEST_FILE)  # a DataFrame
    thomas_test_data = parse(THOMAS_TEST_FILE)      # a list of dictionaries
    test_species_count(spec_test_df, spec_test_data,
                       thomas_test_df, thomas_test_data)
    test_max_level(spec_test_df, spec_test_data,
                   thomas_test_df, thomas_test_data)
    test_filter_range(spec_test_df, spec_test_data,
                      thomas_test_df, thomas_test_data)
    test_mean_attack_for_type(spec_test_df, spec_test_data,
                              thomas_test_df, thomas_test_data)
    test_count_types(spec_test_df, spec_test_data,
                     thomas_test_df, thomas_test_data)
    test_mean_attack_per_type(spec_test_df, spec_test_data,
                              thomas_test_df, thomas_test_data)


if __name__ == '__main__':
    main()
