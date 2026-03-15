#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/13 17:54:48 by juruan              #+#    #+#            #
#   Updated: 2026/03/14 20:46:58 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        try:
            part = arg.split(":")
            inventory[part[0]] = int(part[1])
        except (ValueError, IndexError):
            continue
    total_item = len(inventory)
    total_value = sum(inventory.values())
    print(f"Total items in inventory: {total_value}")
    print(f"Unique item types: {total_item}")

# current inventory
    print("\n=== Current Inventory ===")
# 核心：sorted()
# key=lambda item: item[1] 表示按照“值”（数量）来排序
# reverse=True 表示从大到小（降序）
    sorted_invent = sorted(
        inventory.items(), key=lambda item: item[1], reverse=True)
    for name, count in sorted_invent:
        if count < 2:
            unit = "unit"
        else:
            unit = "units"
        try:
            per = (count / total_value) * 100
        except ZeroDivisionError:
            per = 0.0
        print(f"{name}: {count} {unit} ({per:.1f}%)")

# 假设 sorted_inventory = [('potion', 5), ('armor', 3), ('sword', 1)]
    print("\n=== Inventory Statistics ===")
    most_item_name, most_count = sorted_invent[0]
    if most_count < 2:
        unit = "unit"
    else:
        unit = "units"
    print(f"Moset abundant: {most_item_name} ({most_count} {unit})")
    least_item_name, least_count = sorted_invent[-1]
    if least_count < 2:
        unit = "unit"
    else:
        unit = "units"
    print(f"Least abundant: {least_item_name} ({least_count} {unit})")
# Item CAtegories, create 2 dicts, iterate invent dict to re-distribute items
    print("\n=== Item Categories ===")
    categories = {"Moderate": {}, "Scarce": {}}
    for name, count in inventory.items():
        if count >= 5:
            categories["Moderate"][name] = count
        else:
            categories["Scarce"][name] = count
    print("Moderate:", categories["Moderate"])
    print("Scarce:", categories["Scarce"])

# Suggestions
    print("\n=== Management Suggestions ===")
    suggestion = []
    for name, count in inventory.items():
        if count < 2:
            suggestion.append(name)
    print(f"Restock needed: {', '.join(suggestion)}")

# Generate inventory reports with dictionary operations
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    value_strings = []
    for value in inventory.values():
        value_strings.append(str(value))

    joined_values = ", ".join(value_strings)
    print(f"Dictionary values: {joined_values}")
    exists = 'sword' in inventory
    print(f"Sample lookup - 'sword' in inventory: {exists}")


if __name__ == "__main__":
    inventory_system()
