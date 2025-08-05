"""
Converter module for handling color pair conversions.
"""

from .constants import MAJOR_COLORS, MINOR_COLORS


def color_pair_to_string(major_color, minor_color):
    """Convert a color pair to a string representation.
    
    Args:
        major_color (str): The major color.
        minor_color (str): The minor color.
        
    Returns:
        str: The string representation of the color pair.
    """
    return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
    """Get the color pair from a pair number.
    
    Args:
        pair_number (int): The pair number.
        
    Returns:
        tuple: The major and minor colors.
        
    Raises:
        Exception: If the major or minor index is out of range.
    """
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    """Get the pair number from a color pair.
    
    Args:
        major_color (str): The major color.
        minor_color (str): The minor color.
        
    Returns:
        int: The pair number.
        
    Raises:
        Exception: If the major or minor color is not found.
    """
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1
