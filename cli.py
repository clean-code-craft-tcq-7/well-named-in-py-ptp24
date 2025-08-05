"""
Command-line interface for the color pair application.
"""

import sys
import os
from color_pair import (
    get_color_from_pair_number,
    get_pair_number_from_color,
    generate_reference_manual,
    generate_csv_report
)


def print_usage():
    """Print usage information."""
    print("Usage:")
    print("  python cli.py pair-to-number <major_color> <minor_color>")
    print("  python cli.py number-to-pair <pair_number>")
    print("  python cli.py reference-manual [output_file]")
    print("  python cli.py csv-report [output_file]")
    print("\nExamples:")
    print("  python cli.py pair-to-number White Blue")
    print("  python cli.py number-to-pair 1")
    print("  python cli.py reference-manual manual.txt")
    print("  python cli.py csv-report report.csv")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print_usage()
        return 1
    
    command = sys.argv[1]
    
    if command == "pair-to-number" and len(sys.argv) == 4:
        major_color = sys.argv[2]
        minor_color = sys.argv[3]
        try:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            print(f"Pair number: {pair_number}")
        except Exception as e:
            print(f"Error: {e}")
            return 1
    
    elif command == "number-to-pair" and len(sys.argv) == 3:
        try:
            pair_number = int(sys.argv[2])
            major_color, minor_color = get_color_from_pair_number(pair_number)
            print(f"Major color: {major_color}")
            print(f"Minor color: {minor_color}")
        except ValueError:
            print("Error: Pair number must be an integer")
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 1
    
    elif command == "reference-manual":
        manual = generate_reference_manual()
        if len(sys.argv) == 3:
            output_file = sys.argv[2]
            with open(output_file, 'w') as f:
                f.write(manual)
            print(f"Reference manual written to {output_file}")
        else:
            print(manual)
    
    elif command == "csv-report":
        csv = generate_csv_report()
        if len(sys.argv) == 3:
            output_file = sys.argv[2]
            with open(output_file, 'w') as f:
                f.write(csv)
            print(f"CSV report written to {output_file}")
        else:
            print(csv)
    
    else:
        print_usage()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
