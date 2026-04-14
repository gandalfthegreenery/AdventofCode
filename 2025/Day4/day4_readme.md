# Advent of Code 2025 – Day 4:

## Overview

This repository contains solutions to Day 4 of the 2025 Advent of Code challenge.

The problem involves analyzing a 2D grid of symbols and identifying elements based on the number of neighboring cells. The solution also extends to an iterative removal process based on these neighbor counts.

---

## Problem Description

You are given a 2D grid consisting of:

* `@` → occupied cell
* `.` → empty cell

Each row of the input corresponds to a row in the grid.

---

## Objectives

### Part 1

Count the number of `@` cells that have **fewer than 4 neighboring `@` cells**.

* Neighbors include all **8 surrounding positions** (including diagonals)

---

### Part 2

Simulate the following process:

1. Remove all `@` cells with fewer than 4 neighbors
2. Update neighbor counts
3. Repeat until no more cells can be removed

Return the **total number of removed `@` cells**.

---

## Approach

### Neighbor Accumulation

Instead of checking neighbors individually for each cell, this solution builds a **neighbor count grid**:

* A separate 2D array (`neighbors`) is maintained
* For every `@` cell:

  * Increment all values in its surrounding **3×3 region**
  * Subtract 1 from the center to avoid counting itself

This allows neighbor counts to be retrieved in **constant time**.

---

### Data Structures

* `rolls` → stores the original grid (`@` / `.`)
* `neighbors` → stores the number of adjacent `@` cells for each position

The neighbor grid is padded to simplify boundary handling.

---

## Part 1 Solution

After building the neighbor grid:

* Iterate through all valid grid positions
* Count cells where:

  ```python
  rolls[i][j] == "@" and neighbors[i+1][j+1] < 4
  ```

---

## Part 2 Solution: Iterative Removal

This part simulates a **stability process**:

1. Loop until no more changes occur
2. For each `@` cell:

   * If it has fewer than 4 neighbors:

     * Remove it
     * Update the neighbor grid (subtract its influence)
3. Track the total number of removed cells

---

## Key Insight

The iterative process is similar to a **grid-based pruning algorithm**:

* Each removal affects neighboring cells
* This may cause new cells to fall below the threshold
* The process continues until a stable configuration is reached

---

## Usage

1. Place input file in the project directory:

   ```
   AdventofCodeDay4.txt
   ```

2. Run:

```bash 
python solution.py
```

---

## Performance

| Step                       | Complexity | Notes                        |
| -------------------------- | ---------- | ---------------------------- |
| Neighbor grid construction | O(n²)      | Single pass over grid        |
| Each iteration             | O(n²)      | Checks all cells             |
| Total                      | O(k · n²)  | k = number of removal rounds |

---

## Key Insights

* Precomputing neighbor counts avoids repeated local scans
* Padding simplifies boundary conditions
* The iterative removal behaves like a **cascade or erosion process**
* Efficient updates prevent recomputing the entire grid each iteration

---

## Future Improvements

* Track only “active” cells to reduce repeated full-grid scans
* Use a queue-based approach to process newly unstable cells
* Improve readability by separating grid logic into helper functions

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
