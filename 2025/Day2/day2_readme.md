These are solutions for day 2 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/2
# Advent of Code 2025 – Day 2:

## Overview

This repository contains solutions to Day 2 of the 2025 Advent of Code challenge.

The problem involves identifying and summing numbers within given ranges that exhibit **repeated digit patterns**. Two variations are considered:

* **Part 1:** Numbers formed by repeating a pattern exactly twice
* **Part 2:** Numbers formed by repeating a pattern any number of times

The key challenge is handling extremely large ranges efficiently (up to 12-digit numbers) without brute-force iteration.

---

## Problem Description

You are given a list of numeric ranges in CSV format:

```
xxxx-yyyy, zzzzzzz-aaaaaaaa
```

Each range defines a search interval ([start, end]).

A number is considered valid if it can be constructed by repeating a smaller digit pattern. For example:

```
4545 = (45)(45)
777777 = (7)(7)(7)(7)(7)(7)
```

---

## Objectives

### Part 1

Sum all values within each range that consist of a pattern repeated **exactly twice**.

### Part 2

Sum all values within each range that consist of a pattern repeated **any number of times**.

---

## Approach

### ❌ Naive Approach (Not Used)

A brute-force solution would:

* Iterate through every number in each range
* Check whether it forms a repeated pattern

This becomes computationally infeasible for large ranges (up to (10^{12})).

---

### ✅ Optimized Pattern Generation

Instead of checking every number, this solution:

1. **Identifies valid pattern lengths**

   * For a number with (n) digits, valid pattern lengths must divide (n)
   * Pattern length must be ≤ (n/2)

2. **Generates candidate patterns directly**

   * For each valid pattern length (k):

     * Iterate over all possible base patterns of length (k)
     * Construct full numbers by repeating the pattern

3. **Filters candidates within range**

   * Only include values between `start` and `end`

4. **Avoids double-counting**

   * Ensures numbers generated from smaller patterns (e.g., `22`, `33`) are not counted multiple times

---

## Example

Range:

```id=
123456 - 678910
```

Valid pattern lengths:

* 1 → generates values like `111111`, `222222`, ...
* 2 → generates `121212`, `343434`, ...
* 3 → generates `123123`, `456456`, ...

Only values within the range are included in the final sum.

---

## Implementation Details

Helper functions are used for each pattern length:

* `checking_halves` → patterns repeated 2 times
* `checking_thirds` → patterns repeated 3 times
* `checking_fifths` → patterns repeated 5 times
* `checking_sevenths` → patterns repeated 7 times

Each function:

* Adjusts range boundaries to match valid digit lengths
* Iterates over base patterns
* Constructs repeated values using string multiplication
* Accumulates valid sums

---

## Usage

1. Place input file in the project directory:

   ```
   AdventofCodeDay2.txt
   ```

2. Run:

```bash 
python solution.py
```

---

## Performance

| Approach      | Time Complexity       | Notes                                  |
| ------------- | --------------------- | -------------------------------------- |
| Brute Force   | O(range size)         | Infeasible for large inputs            |
| This Solution | O(number of patterns) | Efficient due to structured generation |

---

## Key Insights

* Repeated-pattern numbers are **highly structured**, allowing direct generation
* Valid candidates can be derived from **factorizations of digit length**
* Avoiding brute force dramatically improves performance on large ranges
* Careful handling is required to prevent **duplicate counting across pattern sizes**

---

## Future Improvements

* Generalize helper functions into a single parameterized routine
* Add validation tests for overlapping pattern cases
* Improve readability by consolidating repeated logic

---
