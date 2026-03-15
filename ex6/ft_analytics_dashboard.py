#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/15 12:51:00 by juruan              #+#    #+#            #
#   Updated: 2026/03/15 18:37:54 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def player_info() -> list:
    p1 = ("alice", 2300)
    p2 = ("bob", 1800)
    p3 = ("charlie", 2150)
    p4 = ("diana", 2050)
    return [p1, p2, p3, p4]


def player_active() -> list:
    p1 = ("alice", 10)
    p2 = ("bob", 15)
    p3 = ("charlie", 11)
    p4 = ("diana", 8)
    return [p1, p2, p3, p4]


def player_region() -> list:
    p1 = ("alice", "north")
    p2 = ("bob", "central")
    p3 = ("charlie", "east")
    return [p1, p2, p3]


def ft_analytics_dashboard() -> None:
    print("=== Game Analytic Dashboard ===")
    print()

    players = player_info()
    active_times = player_active()
    regions = player_region()

    achievement_counts_source = {
        "alice": ["a", "b", "c", "d", "e"],
        "bob": ["a", "b", "c"],
        "charlie": ["a", "b", "c", "d", "e", "f", "g"]
    }

    achievement_sets_source = [
        ["first_kill", "level_10"],
        ["boss_slayer", "first_kill"],
        ["level_10"]
    ]

# List Comprehension
    print("=== List Comprehension Examples ===")
    high_scorer = [name for name, score in players if score > 2000]
    double_score = [score * 2 for name, score in players]
    active_p = [
        name for name, active_time in active_times if active_time >= 10
    ]
    print(f"High scorers (>2000): {high_scorer}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {active_p}")

# Dict Comprehension
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {name: score for name, score in players}
    print(f"Player scores: {player_scores}")

    scores = [score for name, score in players]
    categories = {
        "high": len([s for s in scores if s >= 2200]),
        "medium": len([s for s in scores if 2000 <= s < 2200]),
        "low": len([s for s in scores if s < 2000])
    }
    print(f"Score categories: {categories}")

    achievement_counts = {
        player: len(achievement_counts_source[player])
        for player in achievement_counts_source
    }
    print(f"Achievement counts: {achievement_counts}")

# Set Comprehension
    print("\n=== Set Comprehension Examples ===")
    unique_players = {name for name, score in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for player in achievement_sets_source for ach in player
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {region for name, region in regions}
    print(f"Active regions: {active_regions}")

# Combined Analysis
    print("\n=== Combined Analysis ===")

    total_players = len(player_info())
    print(f"Total players: {total_players}")

    count_unique_ach = len(unique_achievements)
    print(f"Total unique achievements: {count_unique_ach}")

    average_score = sum([score for name, score in players]) / total_players
    print(f"Average score: {average_score}")

    max_score = max(scores)
    top_player = [name for name, score in players if score == max_score][0]
    achievement_counts = {
        player: len(achs) for player, achs in achievement_counts_source.items()
    }
    top_ach = achievement_counts[top_player]
    print(
        f"Top performer: {top_player} "
        f"({max_score} points, {top_ach} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
