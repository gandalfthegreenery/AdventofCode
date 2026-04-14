# Advent of Code 2025 – Day 1: Dial Lock Simulation

## Overview

This repository contains solutions to Day 1 of the 2025 Advent of Code challenge.

The problem involves simulating a 100-position dial lock and counting how often the dial:

* **lands on 0** (Part 1), or
* **passes over or lands on 0** (Part 2)

Two approaches are implemented:

1. A direct simulation method
2. An optimized state-based method that reduces redundant computation

---

## Problem Description

You are given a sequence of dial movements in the format:

```
L(R)XXXX
```

Where:

* `L` = rotate left (decreasing values)
* `R` = rotate right (increasing values)
* `XXXX` = number of steps to rotate (positive integer)

The dial:

* has values from `0` to `99`
* wraps around modulo 100
* starts at position **50**

---

## Objectives

### Part 1

Count the number of times the dial **lands exactly on 0** after each move.

### Part 2

Count the number of times the dial **passes over or lands on 0**, including during large rotations that span multiple full cycles.

---

## Approach

### Solution 1: Direct Simulation

This approach:

* Updates the dial position for each instruction
* Uses modulo arithmetic to wrap values
* Increments the count when the dial lands on 0

#### Key Idea

```python
if current_dial % 100 == 0:
    count += 1
```

#### Characteristics

* Simple and easy to understand
* Does not account for intermediate crossings of 0 during large rotations
* Suitable for Part 1 only

---

### Solution 2: Optimized Cycle-Based Counting

This approach improves efficiency and correctness for Part 2 by:

1. **Decomposing movement into:**

   * Full rotations (`num // 100`)
   * Remaining steps (`num % 100`)

2. **Counting full rotations directly**

   * Each full rotation guarantees one pass over 0

3. **Handling the remainder carefully**

   * Tracks whether the dial crosses or lands on 0
   * Uses state (`zero`) to avoid double-counting edge cases

#### Key Insight

Instead of simulating every step, we exploit the structure of the problem:

> Every full 100-step rotation contributes exactly one crossing of 0.

This reduces unnecessary computation and ensures correctness for large inputs.

---

## Usage

1. Place your input file in the project directory:

   ```
   AdventofCodeDay1.txt
   ```

2. Run either solution:

```bash
python solution1.py
python solution2.py
```

---

## Example

Input:

```
R150
L75
R50
```

Output:

```
<integer count>
```

---

## Performance

| Solution   | Time Complexity | Notes                                     |
| ---------- | --------------- | ----------------------------------------- |
| Solution 1 | O(n)            | Simple, but misses intermediate crossings |
| Solution 2 | O(n)            | Handles large rotations efficiently       |

---

## Key Takeaways

* Leveraging problem structure (modulo cycles) can significantly simplify computation
* Separating full cycles from remainders is a powerful optimization technique
* Careful state tracking is required to avoid edge-case double counting

---

## Future Improvements

* Add unit tests for edge cases (e.g., starting at 0, exact multiples of 100)
* Refactor into reusable functions/modules
* Extend visualization of dial movement for debugging

---

## Author

Developed by Jacob Ennis as part of the Advent of Code 2025 challenge.
