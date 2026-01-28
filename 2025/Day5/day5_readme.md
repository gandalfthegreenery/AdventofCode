These are solutions for day 5 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/5

But to summarize, the goal is to find the number unique values in a set of ranges that have the ability to overlap. 

for example, given the ranges 
3-4,
4-7,
9-11,
4-12, 
the correct answer should be 9 (3,4,5,6,7,8,9,10,11,12) 

This was accomplished by using a nlog(n) built-in sorting algorithm to initially sort the ranges based on the first value then using a starting iterator and ending iterator
to pass through th list, connecting overlapping ranges and taking the difference of the high and low values for each connected range, and adding it to the running tally before
moving on to the next range.
