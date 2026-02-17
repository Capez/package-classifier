# All inputs: dimensions in cm, mass in kg
VOLUME_LIMIT_CM3 = 1_000_000
DIM_LIMIT_CM = 150
MASS_LIMIT_KG = 20


def sort(width, height, length, mass):
    """Returns stack name: STANDARD, SPECIAL, or REJECTED. width/height/length in cm, mass in kg."""
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("dimensions and mass must be non-negative")
    volume = width * height * length
    bulky = (
        volume >= VOLUME_LIMIT_CM3
        or width >= DIM_LIMIT_CM
        or height >= DIM_LIMIT_CM
        or length >= DIM_LIMIT_CM
    )
    heavy = mass >= MASS_LIMIT_KG
    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
