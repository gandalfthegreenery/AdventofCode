# Advent of Code 2025 – Day 6:

## Overview

This repository contains solutions to Day 6 of the 2025 Advent of Code challenge.

The problem involves parsing a custom-formatted input file containing:

* numeric values
* operation symbols (`+` or `*`)
* structured layouts that must be interpreted across rows and columns

The goal is to evaluate each equation according to its associated operator and compute a total sum.

---

## Problem Description

The input consists of a structured grid-like format where:

* Each equation contains multiple integer values
* Each equation is associated with an operator (`+` or `*`)
* Values may be distributed across rows or columns depending on the encoding scheme

---

## Objective

Evaluate all equations using their corresponding operator and compute the final sum.

---

## Approach

Two different parsing strategies were used depending on the part of the problem.

---

## Part 1: Row-Based Parsing

### Strategy

The input is interpreted in a structured row format:

* First, integer values are stored in a fixed-width buffer
* Then, a corresponding operator is assigned per equation
* Each equation is evaluated independently

### Evaluation Rules

For each equation:

* If operator is `*`: multiply all values
* If operator is `+`: sum all values

---

### Key Idea

The problem reduces to:

> Parsing structured input into aligned (values, operator) pairs, then applying a fold operation.

---

## Part 2: Column-Based State Machine Parsing

### Strategy

The second interpretation treats the input as a **column-stream encoding**, requiring:

* Reading the input column-by-column
* Maintaining a rolling buffer of values (`eq_buf`)
* Tracking the current operator (`current_func`)
* Flushing the buffer whenever a new operator is encountered

---

### Core Mechanism

A helper function is used to evaluate buffered values:

```python 
def clear_buff():
    if current_func == "+":
        temp_val = sum(eq_buf)
    elif current_func == "*":
        temp_val = 1
        for v in eq_buf:
            temp_val *= v
```

After evaluation:

* The buffer is cleared
* The result is added to the global total
* Parsing continues

---

## Key Insight

This problem is fundamentally about:

> Interpreting a serialized 2D structure as a sequence of independent arithmetic expressions

Depending on layout encoding, it can be solved via:

* row-wise parsing (structured tables)
* column-wise reconstruction (stream decoding)

---

## Algorithm Complexity

| Step       | Complexity           |
| ---------- | -------------------- |
| Parsing    | O(n × m)             |
| Evaluation | O(k) per equation    |
| Total      | Linear in input size |

---

## Key Insights

* Input is effectively a **transposed representation of expressions**
* Operator tokens act as **delimiters for buffer flushing**
* The solution behaves like a lightweight **streaming parser**
* State management is critical to correctly grouping operands

---

## Usage

1. Place input file in the project directory:

   ```
   AdventofCodeDay6.txt
   ```

2. Run:

```bash 
python solution.py
```

---

## Future Improvements

* Refactor parsing into a reusable tokenizer
* Replace manual buffering with a formal parser (e.g., state machine class)
* Improve robustness for malformed inputs
* Separate evaluation logic from parsing logic for clarity

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
