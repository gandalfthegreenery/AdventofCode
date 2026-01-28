These are solutions for day 7 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/7

But to summarize, there is scenairo analogous to a galton-machine (https://en.wikipedia.org/wiki/Galton_board) where given an input of a series 
of characters with . representing empty space, and ^ representing the physical location of a peg. For part 1, the goal is to calculate the number of possible bins 
at the bottom of the board (represented by the final line of the file) that a ball dropped from the very top could end up in. For part 2, the goal was to calculate
the number of potential paths the ball could have taken to end up in one of those possible bins. 

This was accomplished in part 1 by creating a positions array, which is passes from row to row. If a position in the positions array equals the position of a peg in the board,
then the two adjacent positions are added to the positions array, and the current position removed, corresponding to the available spots that the ball could have fallen (L or right of peg, but not at peg).

In part 2, the same basic function was accomplished, but instead of just including the presence of positions, when adjacent squares are combined, the sum of the top two are added together, creating a pascal's triangle-like solution.

