# Advent of Code 2025 – Day 3: 

## Overview

This repository contains solutions to Day 3 of the 2025 Advent of Code challenge.

The problem involves selecting a substring of fixed length from a larger numeric string such that the resulting number is maximized. The selected values are then summed across all input lines.

Two variations are considered:

* **Part 1:** Select the maximum 2-digit substring
* **Part 2:** Select the maximum 12-digit substring

---

## Problem Description

You are given a list of numeric strings:

* Each string is 100 digits long
* Each line is processed independently

The task is to:

1. Select a substring of fixed length (k)
2. Ensure digits remain in their original order
3. Maximize the resulting numeric value
4. Sum the results across all rows

---

## Key Insight

A brute-force approach would:

* Check all possible substrings of length (k)
* Compare their numeric values

This is inefficient for larger (k), especially across many rows.

---

## Approach: Greedy Selection

This solution uses a **greedy algorithm** to construct the optimal substring from right to left.

### Core Idea

At each position:

* Choose the **largest possible digit** that still allows completion of the substring
* Once a digit is selected, all future selections must come from positions **to its right**

---

## Example

Input:

```
98765432100088
```

Goal: find the largest 2-digit substring.

### Process

Start from the end:

```
...0088  → initial candidate
```

Scan leftward:

* Ignore digits smaller than current candidate
* Replace when a larger or equal digit is found

Progression:

```
98765432100088
           ↑ start

...000 → ignored  
...1   → ignored  
...2   → ignored  
...8   → replaces first digit  
9 8 765432100088  
↑ ↑

9 found → improves further:
98 765432100088
```

Final result:

```
98
```

---

## Implementation Details

The algorithm:

1. Initializes a set of candidate positions from the end of the string
2. Iteratively scans backward to find better digit choices
3. Updates positions while maintaining ordering constraints
4. Constructs the final substring from selected indices

This ensures:

* Optimal selection at each step
* No need to evaluate all substrings explicitly

---

## Usage

1. Place input file in the project directory:

   ```
   AdventofCodeDay3.txt
   ```

2. Run:

```bash
python solution.py
```

---

## Performance

| Approach               | Time Complexity     | Notes                                          |
| ---------------------- | ------------------- | ---------------------------------------------- |
| Brute Force            | O(n · k) per row    | Checks all substrings                          |
| Greedy (this solution) | O(n · k) worst-case | Efficient in practice, avoids full enumeration |

---

## Key Insights

* The problem can be reframed as selecting a **maximum lexicographic subsequence of fixed length**
* Greedy selection works because earlier digits have higher positional weight
* Maintaining ordering constraints is critical to correctness
* Backward scanning ensures all viable candidates are considered efficiently

---

## Future Improvements

* Refactor debug-heavy Part 2 implementation for clarity
* Generalize solution for arbitrary substring lengths
* Explore stack-based implementations for improved readability

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
