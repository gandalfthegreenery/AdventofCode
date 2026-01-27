These are solutions for day 2 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/2

But to summarize, the goal is to find the sum of all numbers within given ranges that have a repeated pattern of digits. For example, 4544-4546 would have 4545 as a valid repeated pattern of digits (45)(45). 

The input is a series of ranges in csv format, for example the input xxxx-yyyy, zzzzzzz-aaaaaaaa would refer to two ranges from xxxx to yyyy and zzzzzzz to aaaaaaaa that must be searched for repeated values.
Submission 1 is a simple counter that increments anytime the current value modulo 100 is 0.
