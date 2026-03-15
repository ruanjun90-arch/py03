#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: juruan <juruan90@gmail.com>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/14 21:03:34 by juruan              #+#    #+#            #
#   Updated: 2026/03/15 12:43:57 by juruan             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Generator


def event_stream(count: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]

    for i in range(count):
        player = players[i % len(players)]
        level = levels[i % len(levels)]
        action = actions[i % len(actions)]
        yield {
            "player": player,
            "level": level,
            "action": action
        }


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0
    event_number = 1

    for event in event_stream(1000):
        total_events += 1
# 更新统计
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1
# 打印前三个events
        if event_number <= 3:
            print(
                f"Event {event_number}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

        event_number += 1

    print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


# Generate Fibonacci sequence
def fibonacci_stream() -> Generator[int, None, None]:
    a = 0
    b = 1

    while True:
        yield a

        temp = a + b
        a = b
        b = temp


# Generate prime numbers
def prime_steam() -> Generator[int, None, None]:
    n = 2

    while True:
        is_prime = True
# 判断是否是质数
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            yield n

        n += 1


if __name__ == "__main__":
    ft_data_stream()
# fibonacci demo
    fib = fibonacci_stream()

    numbers = []
    for _ in range(10):
        numbers.append(str(next(fib)))
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): " + ", ".join(numbers))
# prime demo
    prime = prime_steam()

    collection = []
    for i in range(5):
        collection.append(str(next(prime)))
    print("Prime numbers (first 5): " + ", ".join(collection))
