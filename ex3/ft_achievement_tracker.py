#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/13 09:00:35 by juruan              #+#    #+#            #
#   Updated: 2026/03/13 17:31:56 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_achievement_tracker() -> None:
    # 1. 初始化数据
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    # 2. 所有的唯一成就 (并集)
    unique_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    # 3. 所有玩家共同拥有的 (交集)
    # 提示：intersection
    common = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")

    # 4. 寻找稀有成就 (仅被 1 个玩家拥有的)
    only_alice = alice.difference(bob, charlie)
    only_bob = bob.difference(alice, charlie)
    only_charlie = charlie.difference(alice, bob)
    rare = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare}\n")

    # 5. Alice vs Bob 的对比
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
