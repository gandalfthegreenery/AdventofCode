These are solutions for day 3 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/3

But to summarize, the goal is to find the highest value possible by selecting a substring of length 2 (for part 1) or 12 (part 2) from a larger string of digits, whose numerical
value is the maximum possible for said input string, then summing all of those values.

The input is a series of strings, each 100 values long separated by a newline character.

Both submissions solve this problem with a greedy approach, starting by looking at the final n characters, and iterating towards the front, only modifying the position of a digit if it
is equal to or higher than the current value. 

For example: given the following number, and the goal of trying to find the highest 2-digit substring:

Input: 98765432100088 
Start by taking the final 2 digits, 88, and incrementing a counter backwards, only replacing the first digit if a number >=8 is found.
987654321000**88**
987654321000**88**
           0 not greater than 8
          0 not greater than 8
         0 ""
        1 ""
       2 ""
      3 ""
     4 ""
    5 ""
   6 ""
  7 ""
 8 - equal to 8, so replace first digit with this one, and move all "selected" digits forward along path
9**8**7654321000**8**8
9 - greater than 8, so repeat process:
**98**765432100088, 
At this point we reached the front of the line, so 98 is the largest 2-digit substring of this number.
        
