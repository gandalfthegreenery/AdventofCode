# Advent of Code 2025 – Day 5: Unique Values in Overlapping Ranges

## Overview

This repository contains solutions to Day 5 of the 2025 Advent of Code challenge.

The problem involves determining the total number of **unique integer values** covered by a set of possibly overlapping ranges.

---

## Problem Description

You are given a list of ranges in the format:

```
start-end
```

Each range represents all integer values from `start` to `end` (inclusive).

---

## Objective

Compute the total number of **distinct integers** covered by all ranges, accounting for overlaps.

---

## Example

Input:

```
3-4
4-7
9-11
4-12
```

Merged coverage:

```
3-12
```

Result:

```
10
```

(Values: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

---

## Approach

### Step 1: Sort Ranges

Ranges are sorted by their starting value:

```python 
sorted_ranges = sorted(ranges)
```

This enables efficient merging in a single pass.

---

### Step 2: Merge Overlapping Ranges

Iterate through the sorted ranges while maintaining a current interval:

* If the next range overlaps:

  ```python 
  if low <= prev_high:
      prev_high = max(prev_high, high)
  ```

* Otherwise:

  * Finalize the current range
  * Add its size to the total
  * Start a new range

---

### Step 3: Accumulate Total Coverage

Each merged range contributes:

```python
prev_high - prev_low + 1
```

The `+1` accounts for inclusive endpoints.

---

## Algorithm Complexity

| Step    | Complexity |
| ------- | ---------- |
| Sorting | O(n log n) |
| Merging | O(n)       |
| Total   | O(n log n) |

---

## Key Insights

* Sorting transforms the problem into a **linear merge pass**
* Overlapping intervals can be collapsed into a single range
* This avoids explicitly enumerating values
* The approach scales efficiently for large inputs

---

## Usage

1. Place input file in the project directory:

   ```
   AdventofCodeDay5.txt
   ```

2. Run:

```bash 
python solution.py
```

---

## Future Improvements

* Support open/closed interval variations
* Add input validation for malformed ranges
* Extend to floating-point intervals if needed

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
