# Advent of Code 2025 – Day 7: 

## Overview

This repository contains solutions to Day 7 of the 2025 Advent of Code challenge.

The problem models a **Galton board-like system**, where a particle is dropped from the top of a grid and interacts with obstacles that split its path left or right.

---

## Problem Description

You are given a grid where:

* `.` represents empty space
* `^` represents a peg (splitter)
* `S` marks the starting position at the top

Each peg causes a particle reaching that position to split into two paths:

* One moving left
* One moving right

---

## Objectives

### Part 1: Reachable End States

Determine how many unique bottom bins (final row positions) are reachable from the starting position.

---

### Part 2: Path Counting

Compute the total number of distinct paths that can reach each bin.

This is equivalent to counting how many ways a particle can traverse the board under the splitting rules.

---

## Approach

## Core Idea

The system is modeled as **layer-by-layer propagation of states**, where each row transforms the set of possible positions in the row above.

---

## Part 1: Reachability Propagation

### State Representation

* Maintain a list of active positions (`beams`)
* Each position represents a possible location of the particle at a given row

---

### Transition Rule

For each row:

* If a position contains a peg (`^`):

  * The particle splits into:

    * `i - 1`
    * `i + 1`
* Otherwise:

  * The particle continues straight down

Duplicate positions are removed to track only reachability.

---

### Interpretation

This behaves like a **boolean propagation automaton**:

* Each row computes the reachable set from the previous row
* Final result counts distinct reachable bins

---

## Part 2: Path Counting (Dynamic Programming Version)

### State Representation

Instead of tracking only positions, we track:

> the number of ways to reach each position

This converts the system into a **weighted propagation model**.

---

### Transition Rule

For each position `i`:

* If `i` is a peg:

  * Split its weight:

    * Add to `i - 1`
    * Add to `i + 1`
* Else:

  * Carry weight forward unchanged

This is equivalent to updating a 1D DP array per row.

---

## Key Insight

This system is structurally equivalent to:

* A **directed acyclic graph (DAG)** over grid layers
* Or a **Pascal’s triangle-like convolution process**

Each row performs a local linear transformation of the state vector.

---

## Example Behavior

A single particle at the top evolves like:

```
Row 0:        1
Row 1:       1 1
Row 2:      1 2 1
Row 3:     1 3 3 1
```

with pegs acting as constraints that redirect propagation.

---

## Algorithm Complexity

| Step           | Complexity        |
| -------------- | ----------------- |
| Row processing | O(n)              |
| Total          | O(rows × columns) |

Both parts run in linear time relative to grid size.

---

## Key Insights

* The system is a **state propagation graph over time**
* Part 1 tracks **reachability (boolean state)**
* Part 2 tracks **path counts (integer weights)**
* Pegs act as **branching operators**
* The problem reduces to repeated application of a **linear transition function**

---

## Usage

1. Place input file in project directory:

   ```
   AdventofCodeDay7.txt
   ```

2. Run:

```bash 
python solution.py
```

---

## Future Improvements

* Formalize as matrix multiplication over sparse transition matrices
* Replace list operations with NumPy vectorized updates
* Extend to probabilistic weighting (random walk interpretation)

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
