# Advent of Code 2025 – Day 10: Machine Initialization System

This solution addresses Day 10 of Advent of Code 2025.

Problem link: https://adventofcode.com/2025/day/10

---

## Problem Overview

Each input line describes a machine with three components:

[indicator lights] (button schematics) {joltage requirements}


Example:
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}


Each line contains:

### 1. Indicator light diagram
- A binary target state (on/off per light)
- Initially all lights are off

### 2. Button wiring schematics
- Each button toggles a subset of lights
- Each press flips those lights (0 ↔ 1)

### 3. Joltage requirements (ignored in Part 1, used in Part 2)
- A vector of numeric targets per counter
- Each button can also affect counters instead of lights

---

#  Part 1 – Minimum Button Presses (Light Configuration)

## Goal

Determine the **minimum number of button presses** required to reach the target indicator light configuration.

Each button:
- flips a subset of lights
- may be pressed multiple times
- operations are linear over GF(2) (toggle behavior)

---

##  Key Insight


# 🔋 Part 2 – Joltage Optimization (Incremental System)

## Goal

Now interpret the same buttons differently:

- Each button **increments counters instead of toggling lights**
- Each machine has a target joltage vector `{...}`

We must reach the exact target values using minimum button presses.

---

## 🔧 Key Insight

This becomes an **integer linear system over ℤ⁺**:

\[
A x = b
\]

But now:
- no mod 2 behavior
- purely additive system
- integer constraints still apply
- solution space may be underdetermined

---

## 🧮 Method

### Step 1: Rebuild system as integer matrix
- Each button is a column
- Each entry indicates which counters it increments

---

### Step 2: Solve via RREF decomposition

We again compute:

- pivot variables
- free variables
- affine solution space

---

### Step 3: Parameterize solution

\[
x = x_0 + Vt
\]

This expresses all valid button press combinations.

---

### Step 4: Bounded integer search

We restrict free variables using computed bounds:

- derived from maximum required counter values
- ensures finite search space
- reduces complexity to ≤ 3D enumeration

We then:
- enumerate all valid integer `t`
- reconstruct `x`
- validate feasibility
- compute minimum sum of presses



