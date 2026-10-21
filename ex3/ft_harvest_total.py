#!/usr/bin/env python3
def ft_harvest_total():
    d_1 = int(input("Day 1 harvest: "))
    d_2 = int(input("Day 2 harvest: "))
    d_3 = int(input("Day 3 harvest: "))
    total = d_1 + d_2 + d_3
    print(f"Total harvest: {total}")


if __name__ == "__main__":
    ft_harvest_total()
