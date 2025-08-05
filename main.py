
"""
Main module for the color pair application.
"""

from color_pair import tests
from color_pair import report_tests


if __name__ == '__main__':
    # Run conversion tests
    tests.run_tests()
    
    # Run report tests
    report_tests.run_report_tests()
    
    print("All tests completed successfully!")
