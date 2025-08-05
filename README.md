# Automate Package Sorting

This repo automates package sorting for a robotic arm based on package volume and mass.

## Package Classification Rules

- **Bulky Package**: 
  - Volume ≥ 1,000,000 cm³ OR
  - Any dimension ≥ 150 cm
- **Heavy Package**:
  - Mass ≥ 20 kg

## Sorting Categories

- **STANDARD**: Neither bulky nor heavy packages
- **SPECIAL**: Either bulky OR heavy packages (but not both)
- **REJECTED**: Both bulky AND heavy packages

## Usage

```python
from package_sorter import sort

# Example usage
result = sort(width=100, height=100, length=100, mass=15)
print(result)  # expected "STANDARD"
```

## Development

### Install the package in development mode

Make sure you are in the package folder containing `src` and `tests` directories, then run:
```bash
pip install -e .[dev]
```

### Running Tests

```bash
pytest tests/ -v
```

### Running Tests with Coverage

```bash
pytest tests/ --cov=robot_package_automation
```

## Input Requirements

- All dimensions (width, height, length) must be positive numbers in centimeters
- Mass must be a positive number in kilograms
- Zero or negative values will raise ValueError