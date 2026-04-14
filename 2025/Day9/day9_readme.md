# Advent of Code 2025 – Day 9: 

This solution addresses Day 9 of Advent of Code 2025.

Problem link: https://adventofcode.com/2025/day/9

---

## Problem Summary

We are given a set of **red tile coordinates** on a 2D grid.

### Part 1
Find the **largest rectangle** that can be formed using any two red tiles as opposite corners.

The rectangle may include any tiles in between.

---

### Part 2
A constraint is added:

- Red tiles form a closed loop connected by green tiles (as described in the problem)
- Only tiles that are **red or green (inside the loop)** are valid for inclusion
- The rectangle must still use red tiles as opposite corners
- But all interior tiles must lie entirely within the valid region

---

## High-Level Approach

This solution is geometry-based and relies on:

### 1. Point representation
Each red tile is represented as a `Point(x, y)`.

### 2. Area computation
For any two points:
area = (|x1 - x2| + 1) * (|y1 - y2| + 1)

---

### Part 2
A constraint is added:

- Red tiles form a closed loop connected by green tiles (as described in the problem)
- Only tiles that are **red or green (inside the loop)** are valid for inclusion
- The rectangle must still use red tiles as opposite corners
- But all interior tiles must lie entirely within the valid region

---

## High-Level Approach

This solution is geometry-based and relies on:

### 1. Point representation
Each red tile is represented as a `Point(x, y)`.

### 2. Area computation
For any two points:


area = (|x1 - x2| + 1) * (|y1 - y2| + 1)


This represents the number of grid cells in the axis-aligned rectangle.

---

## Part 1 Strategy

Instead of checking all O(n²) pairs blindly, the solution:

### Step 1: Sort points by X and Y
This allows quadrant pruning.

### Step 2: Partition into quadrants
Points are grouped into:
- upper-left
- upper-right
- lower-left
- lower-right

### Step 3: Only test valid diagonal pairs
The maximum rectangle must come from:
- upper-left × lower-right
- upper-right × lower-left

### Step 4: Compute maximum area over valid pairs

This reduces unnecessary comparisons significantly.

---

## Part 2 Strategy

Part 2 introduces **a constrained interior region (red + green loop)**.

This is solved by:

### Step 1: Build polygon ordering
Red tiles are linked in sequence (forming a loop).

### Step 2: Determine convex/concave structure
Each point is classified based on traversal direction changes.

### Step 3: Assign possible valid rectangle corners
Each point is labeled with valid corner roles:
- top-left (tl)
- top-right (tr)
- bottom-left (bl)
- bottom-right (br)

### Step 4: Validate candidate rectangles
Each candidate corner pair is filtered using directional constraints:
- monotonic traversal limits
- boundary consistency checks
- validity against loop structure

### Step 5: Track maximum valid area

---

## Key Classes

### `Point`
Represents a tile with:
- coordinates
- polygon connectivity (next/prev)
- geometric classification
- directional metadata

### `Line`
Used for detecting geometric relationships between edges:
- parallel overlap detection
- perpendicular intersection checks
- corner adjacency detection

---

## Complexity

- Sorting: **O(n log n)**
- Pair evaluation: reduced from O(n²) via quadrant pruning
- Part 2: constrained traversal over polygon boundary

---

## Summary

- Part 1: optimized brute-force over structured quadrants
- Part 2: polygon-constrained geometric validation
- Key idea: reduce search space via spatial structure + traversal constraints
