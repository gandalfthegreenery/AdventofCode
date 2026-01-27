These are solutions for day 1 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/1

But to summarize, the goal is to find the number of times a 100 value dial lock lands on (for part 1) or passes over (for part 2) the number 0.

The input is a series of values in the format L(R)XXXX, where L corresponds to a left turn on the dial (values decrease), R corresponds to a right turn on the dial (values increase) and XXXX is any positive integer, referring to how far the dial is turned to the left or right relative to its current position.

Submission 1 is a simple counter that increments anytime the current value modulo 100 is 0.

Submission 2 is a state-based value check, that reduces the distance to the number of whole rotations and a remainder, counts the number of whole rotations, then resolves the remainder by adding it with the current position, and increments once more if there is another pass/landing on zero during this resolution.
