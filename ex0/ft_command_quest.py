#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 18:18:34 by juruan              #+#    #+#            #
#   Updated: 2026/03/12 22:01:57 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    length = len(sys.argv)
    if length < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {length}")
    else:
        received_arg = length - 1
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {received_arg}")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {length}")
        print()


if __name__ == "__main__":
    ft_command_quest()
