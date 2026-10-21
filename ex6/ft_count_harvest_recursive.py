#!/usr/bin/env python3
def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def harvest_countdown(day):
        if day > harvest:
            print("Harvest time!")
            return
        print(f"Day {day}")
        harvest_countdown(day + 1)
    harvest_countdown(1)


if __name__ == "__main__":
    ft_count_harvest_recursive()
