# Advent of Code 2025 — Day 10:

This problem explores two closely related systems disguised in different forms: a **binary toggle puzzle** (Part 1) and a **linear integer system** (Part 2). Both revolve around combining button effects to match a target configuration, but the underlying mathematics shifts dramatically between the two parts.

---

# Problem Format

Each machine is described on a single line:

```
[.##.] (0,2) (1,3) (2,3) ... {3,5,4,7}
```

Where:

* `[...]` → target indicator light configuration
* `(a,b,c)` → a button that affects those indices
* `{...}` → joltage requirements (ignored in Part 1, central in Part 2)

Each line defines an independent machine.

---

# PART 1 — Indicator Light System (Binary Toggle Model)

## Problem Statement

All indicator lights begin in the OFF state. Each button press toggles a fixed subset of lights.

Goal:

> Determine the minimum number of button presses required to reach the target configuration.

Constraints:

* Buttons may be pressed any number of times
* Each press flips the state (ON ↔ OFF) of its assigned lights

---

## Key Insight

This is a **shortest-path problem in an implicit graph**:

* Nodes → all possible light configurations
* Edges → applying a button (toggle operation)
* Start → all lights OFF
* Goal → target configuration
* Cost → number of button presses

Thus, the problem is solved using **Breadth-First Search (BFS)**.

---

## State Representation

A configuration is represented as:

> A set of indices where lights are ON

Example:

```
[.##.] → {1, 2}
```

Each button is similarly represented as a set:

```
(0,2,3) → {0,2,3}
```

This allows transitions to be expressed cleanly as set operations.

---

## Transition Rule

Pressing a button toggles lights via symmetric difference:

```
new_state = current_state XOR button_state
```

This is equivalent to bitwise XOR in a binary vector space (GF(2)^n).

---

## BFS Strategy

The search explores the state space level-by-level:

1. Initialize with reachable states after one button press
2. Track states reachable at each depth (number of presses)
3. Expand by applying every button
4. Stop when the target configuration is reached

This guarantees the first solution found is optimal.

---

## Interpretation

Part 1 can be interpreted as:

> Finding the shortest path in an n-dimensional hypercube, where each button is a fixed vector that flips selected dimensions.

Each button is effectively a basis vector in GF(2)^n, and solutions correspond to combinations of these vectors under XOR.

---

## Complexity

Let:

* N = number of lights
* B = number of buttons

Worst-case complexity:

```
O(2^N)
```

since BFS may explore all possible light configurations.

---

# PART 2 — Joltage System (Integer Linear Model)

## Problem Statement

In Part 2, the same buttons are repurposed:

* Instead of toggling lights, they now **increment joltage counters**
* Each machine has a target vector of joltage values
* Each button increases selected counters by 1

Goal:

> Find the minimum total number of button presses required to exactly match all joltage requirements.

---

## Key Insight

This transforms the problem into an **integer linear system**.

Each button defines a vector in ℤⁿ, and pressing a button corresponds to adding that vector.

We want to find non-negative integers x such that:

```
A x = b
```

Where:

* A = button incidence matrix
* x = number of times each button is pressed
* b = target joltage vector

Objective:

```
minimize sum(x)
```

subject to:

* x ≥ 0
* x ∈ ℤ

---

## Matrix Construction

We construct an augmented system:

```
[A | b]
```

Where:

* Columns correspond to buttons
* Rows correspond to joltage counters
* Entries indicate whether a button affects a counter

---

## Solving Strategy

### Step 1 — Row Reduction

We perform **Gaussian elimination (RREF)** to simplify the system.

This identifies:

* Pivot variables (dependent constraints)
* Free variables (degrees of freedom)

---

### Step 2 — Parameterization

The general solution takes the form:

```
x = x₀ + Vt
```

Where:

* x₀ is a particular solution
* V spans the nullspace
* t are free integer parameters

---

### Step 3 — Integer Feasibility Constraints

We enforce:

* x must be integer
* x ≥ 0
* x must not exceed derived upper bounds

Because free variables are small in practice (≤ 3), we can enumerate valid integer combinations of t.

---

### Step 4 — Optimization

For each valid solution, compute:

```
sum(x)
```

and select the minimum across all feasible solutions.

---

## Interpretation

Part 2 reframes the system as:

> A constrained integer optimization problem over a linear transformation space

It is closely related to:

* Integer Linear Programming (ILP)
* Lattice basis exploration
* Nullspace parameter search under constraints

---

## Complexity

Let:

* n = number of buttons
* k = number of free variables

Then complexity becomes:

```
O(B^k)
```

Since k is small, exhaustive enumeration is tractable.

---

# Final Insight

Both parts describe the same underlying structure:

* Buttons define basis vectors
* Machine state is a combination of those vectors
* The solution is a selection of vectors that reach a target

However, the interpretation changes:

| Part   | Model                       | Method                         |
| ------ | --------------------------- | ------------------------------ |
| Part 1 | Binary state system (GF(2)) | BFS shortest path              |
| Part 2 | Integer vector system (ℤ)   | RREF + constrained enumeration |

---
