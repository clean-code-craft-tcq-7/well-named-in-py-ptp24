"""
Test module for color pair conversions.
"""

from .converter import get_color_from_pair_number, get_pair_number_from_color


def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    """Test conversion from pair number to color pair.
    
    Args:
        pair_number (int): The pair number to test.
        expected_major_color (str): The expected major color.
        expected_minor_color (str): The expected minor color.
    """
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """Test conversion from color pair to pair number.
    
    Args:
        major_color (str): The major color to test.
        minor_color (str): The minor color to test.
        expected_pair_number (int): The expected pair number.
    """
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)


def run_tests():
    """Run all tests for color pair conversions."""
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed :)')
