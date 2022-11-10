"""
Thomas Kanenaga
CSE 163 AD

This file contains the test functions for the homework
problems for HW0 so that I know that the functions are
running correctly.
"""

import hw0
from cse163_utils import assert_equals


def test_funky_sum():
    """
    This function tests the "funk_sum" function by utilizing
    expected output and inputs using the assert_equals
    function.
    """
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(2.2, hw0.funky_sum(1, 3, 0.6))
    assert_equals(100, hw0.funky_sum(100, 3, -1))
    assert_equals(1, hw0.funky_sum(3, 1, 100))
    assert_equals(3, hw0.funky_sum(1, 3, 1))


def test_total():
    """
    This function tests the "total" function by utilizing
    expected output and inputs using the assert_equals
    function.
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    assert_equals(None, hw0.total(-10))


def test_swip_swap():
    """
    This function tests the "swip_swap" function by utilizing
    expected output and inputs using the assert_equals
    function.
    """
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    assert_equals('htomas', hw0.swip_swap('thomas', 't', 'h'))
    assert_equals('tunher', hw0.swip_swap('hunter', 'h', 't'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
