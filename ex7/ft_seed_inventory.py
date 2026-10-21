#!/usr/bin/env python3
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.lower().title()
    if unit.lower() == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit.lower() == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit.lower() == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
