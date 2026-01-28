These are solutions for day 4 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/4

But to summarize, the goal is to find the number of @ symbols in a 2d grid of @ and . symbols who have fewer than 4 @ symbols in any of the adjacent 8 locations. 

The input is a series of strings consisting of @ and . where each line refers to a row, and the position in that line is the column.

This was accomplished by creating a 2d array of the positions of the @ symbols, and another 2d array called neighbors, which is 2 rows and 2 columns larger than the positions array. As the position array is read in from the file, it populates the neighbors array by adding 1 to each value in the 3x3 square neighbors array surrounding the position value.

The first printed line corresponds to the answer for part 1, and just counts the number of entries in the position array(ignoring the outside most columns and rows) which have a corresponding neighbor value <4. 

The second printed line gives the solution to part 2, which asks, if the @ symbols with fewer than 4 neighbors were removed, and this was repeated again and again until all remaining @ symbols have 4 or more neighbors, how many total @ symbols would be removed?
This was accomplished by iterating through the array until there are no changes to it, removing all @ symbols and reducing all neighbor @ values by 1, and incrementing a counter each time an @ symbol is removed.
