"""
Color Pair Package for handling color pair conversions.
"""

from .constants import MAJOR_COLORS, MINOR_COLORS
from .converter import get_color_from_pair_number, get_pair_number_from_color, color_pair_to_string
from .report import generate_reference_manual, generate_csv_report

__all__ = [
    'MAJOR_COLORS',
    'MINOR_COLORS',
    'get_color_from_pair_number',
    'get_pair_number_from_color',
    'color_pair_to_string',
    'generate_reference_manual',
    'generate_csv_report'
]
