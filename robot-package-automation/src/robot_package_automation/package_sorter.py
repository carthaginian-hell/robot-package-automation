"""
Package sorting module for robotic arm automation factory.
"""

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages based on their dimensions and mass.
    
    Args:
        width (float): Width in centimeters
        height (float): Height in centimeters
        length (float): Length in centimeters
        mass (float): Mass in kilograms
        
    Returns:
        str: Sorting category ('STANDARD', 'SPECIAL', or 'REJECTED')
        
    Raises:
        ValueError: If any input is zero or negative
    """
    # Validate inputs
    for value in [width, height, length, mass]:
        if value <= 0:
            raise ValueError("All measurements must be positive numbers")

    # Check if package is bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Check if package is heavy
    is_heavy = mass >= 20

    # Determine category
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"