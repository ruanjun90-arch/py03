#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 20:07:42 by juruan              #+#    #+#            #
#   Updated: 2026/03/12 22:01:30 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    length = len(sys.argv)
    if length == 1:
        message = "No scores provided."
        print(f"{message} Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Oops, invalid score: {score}")
            return

    total_player = len(scores)
    total_score = sum(scores)
    average = total_score / total_player
    max_score = max(scores)
    min_score = min(scores)
    range_score = max_score - min_score
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_player}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    ft_score_analytics()
