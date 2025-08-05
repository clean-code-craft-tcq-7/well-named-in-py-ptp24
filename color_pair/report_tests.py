"""
Tests for the report module.
"""

from .report import generate_reference_manual, generate_csv_report


def test_reference_manual():
    """Test the reference manual generation."""
    manual = generate_reference_manual()
    # Check if manual contains all expected entries
    assert "1" in manual and "White" in manual and "Blue" in manual
    assert "25" in manual and "Violet" in manual and "Slate" in manual
    # Check format
    assert "Pair Number | Major Color | Minor Color" in manual
    
    # Count the number of rows (header + 25 pairs + title + separator)
    rows = manual.strip().split('\n')
    assert len(rows) == 29  # 25 pairs + 4 header lines
    
    print("Reference manual test passed")


def test_csv_report():
    """Test the CSV report generation."""
    csv = generate_csv_report()
    # Check if CSV contains all expected entries
    assert "1,White,Blue" in csv
    assert "25,Violet,Slate" in csv
    # Check header
    assert "PairNumber,MajorColor,MinorColor" in csv
    
    # Count the number of rows (header + 25 pairs)
    rows = csv.strip().split('\n')
    assert len(rows) == 26  # 25 pairs + header
    
    print("CSV report test passed")


def run_report_tests():
    """Run all report tests."""
    test_reference_manual()
    test_csv_report()
    print("All report tests passed :)")
