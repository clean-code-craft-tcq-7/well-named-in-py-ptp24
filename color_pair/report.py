"""
Report module for generating color pair reference manuals.
"""

from .constants import MAJOR_COLORS, MINOR_COLORS
from .converter import get_pair_number_from_color, color_pair_to_string


def generate_reference_manual():
    """Generate a reference manual for color coding.
    
    Returns:
        str: Formatted reference manual.
    """
    manual = "Color Coding Reference Manual\n"
    manual += "===========================\n\n"
    manual += "Pair Number | Major Color | Minor Color\n"
    manual += "----------- | ----------- | -----------\n"
    
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual += f"{pair_number:11} | {major_color:11} | {minor_color}\n"
    
    return manual


def generate_csv_report():
    """Generate a CSV report for color coding.
    
    Returns:
        str: CSV formatted report.
    """
    csv = "PairNumber,MajorColor,MinorColor\n"
    
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            csv += f"{pair_number},{major_color},{minor_color}\n"
    
    return csv
