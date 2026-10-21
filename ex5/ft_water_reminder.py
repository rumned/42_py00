#!/usr/bin/env python3
def ft_water_reminder():
    last_watered = int(input("Days since last watering: "))
    if (last_watered > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")


if __name__ == "__main__":
    ft_water_reminder()
