#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 21:44:43 by juruan              #+#    #+#            #
#   Updated: 2026/03/12 23:37:10 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math
import sys


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()

    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
        coordinate = (x, y, z)
        distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        print(f"Position created: {coordinate}")
        print(f"Distance between (0, 0, 0) and {coordinate}: {distance:.2f}")

    elif len(sys.argv) == 2:
        coord_str = sys.argv[1]
        parts = coord_str.split(",")

        try:
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            coordinate = (x, y, z)
            dist = math.sqrt(x ** 2 + y ** 2 + z ** 2)

            print(f'Parsing coordinates: "{coord_str}"')
            print(f"Parsed position: {coordinate}")
            print(f"Distance between (0, 0, 0) and {coordinate}: {dist:.1f}")

            px, py, pz = coordinate
            print("\nUnpacking demonstration:")
            print(f"Player at x={px}, y={py}, z={pz}")
            print(f"Coordinates: X={px}, Y={py}, Z={pz}")

        except ValueError as e:
            print(f'Parsing invalid coordinates: "{coord_str}"')
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    ft_coordinate_system()
