"""
Test suite for package sorting module.
"""

import pytest
from robot_package_automation.package_sorter import sort

def test_standard_package():
    assert sort(100, 100, 50, 10) == "STANDARD"

def test_bulky_by_volume():
    assert sort(100, 100, 100, 10) == "SPECIAL"  # 1,000,000 cm³

def test_bulky_by_dimension():
    assert sort(151, 50, 50, 10) == "SPECIAL"  # One dimension >= 150cm

def test_heavy_package():
    assert sort(100, 100, 50, 20) == "SPECIAL"  # Mass >= 20kg

def test_rejected_package():
    assert sort(151, 100, 100, 25) == "REJECTED"  # Both bulky and heavy

def test_edge_case_exact_volume():
    assert sort(100, 100, 100, 10) == "SPECIAL"  # Exactly 1,000,000 cm³

def test_edge_case_exact_dimension():
    assert sort(150, 100, 100, 10) == "SPECIAL"  # Exactly 150cm

def test_edge_case_exact_mass():
    assert sort(100, 100, 50, 20) == "SPECIAL"  # Exactly 20kg

def test_invalid_zero_input():
    with pytest.raises(ValueError):
        sort(0, 100, 100, 10)

def test_invalid_negative_input():
    with pytest.raises(ValueError):
        sort(100, -1, 100, 10)