# Advent of Code 2025 – Day 8: 

## Overview

This repository contains solutions to Day 8 of the 2025 Advent of Code challenge.

The problem involves a set of 3D points and requires constructing connectivity between them based on pairwise distances. The task is closely related to **Minimum Spanning Tree (MST)** construction in graph theory.

---

## Problem Description

You are given a list of points in 3D space:

```
x, y, z
```

The goal is to:

### Part 1

Select the **1000 closest point pairs** and analyze the resulting connectivity structure. The objective is to compute the product of the sizes of the three largest connected components formed by these edges.

---

### Part 2

Continue connecting points until the graph becomes fully connected. Then compute a final metric based on the last connections required to achieve full connectivity.

---

## Approach

### Step 1: Graph Construction

Each point is treated as a node in a weighted graph where:

* Nodes = 3D points
* Edge weight = squared Euclidean distance

All pairwise edges are computed:

```python 
(x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2
```

---

### Step 2: Selecting Closest Edges

Instead of sorting all edges (which would be expensive), the solution maintains a **fixed-size priority list**:

* Keep only the N smallest edges (e.g., 1000 or 10000)
* Insert new edges only if they are smaller than the current maximum in the set

This approximates the edge set needed for MST-like construction.

---

### Step 3: Connectivity via Union-Like Merging

Once candidate edges are selected, connectivity is determined by:

* Building adjacency lists (`neighbors_list`)
* Iteratively merging connected components
* Propagating connections across shared nodes

This behaves similarly to a **union-find (disjoint set)** structure, but implemented recursively.

---

## Key Structures

### `Point`

Represents a node in 3D space:

* Stores coordinates `(x, y, z)`
* Computes squared distance to other points

---

### `Circuit`

Represents a connected component:

* Stores a set of nodes
* Tracks internal edge distance (for initial pairing)
* Supports merging of components

---

## Connectivity Propagation

A recursive helper function is used:

```python 
search_and_add(neighbors_list, current_point, root_point, checked_points)
```

This function:

* Traverses adjacency relationships
* Expands connected components
* Prevents revisiting nodes via a visited map

---

## Part 1 Interpretation

The system:

1. Keeps the 1000 shortest edges
2. Builds partial connectivity graph
3. Extracts connected component sizes
4. Computes final product of largest components

This approximates a **partial MST forest construction**.

---

## Part 2 Interpretation

The second phase behaves like a **union-find (disjoint set) algorithm**:

* Each point starts in its own set
* Edges are processed in increasing order
* Sets are merged when edges connect distinct components
* Process continues until all nodes share the same root

This is equivalent to Kruskal’s algorithm without full optimization.

---

## Algorithm Complexity

| Step               | Complexity                 |
| ------------------ | -------------------------- |
| Pairwise distances | O(n²)                      |
| Edge filtering     | O(n² log k) (with pruning) |
| Union propagation  | O(n²) worst case           |

---

## Key Insights

* The problem is fundamentally a **graph connectivity + MST approximation task**
* Squared distances avoid unnecessary square roots
* Maintaining only top-N edges is a heuristic optimization
* Recursive merging mimics **disjoint-set union operations**
* Full connectivity is achieved via edge relaxation in increasing order

---

## Future Improvements

* Replace manual merging with a proper **Union-Find (Disjoint Set Union)** structure
* Use a heap (`heapq`) instead of repeated sorting for edge selection
* Avoid full O(n²) edge enumeration via spatial partitioning (e.g., KD-tree)
* Separate MST construction cleanly (Kruskal’s algorithm implementation)

---

## Usage

1. Place input file in the project directory:

```
AdventofCodeDay8.txt
```

2. Run:

```bash 
python solution.py
```

---

## Disclaimer

All problem-solving, implementation, and final code in this repository were completed by me.

AI tools were occasionally used to support understanding of concepts, debugging, and to help refine written explanations. All final solutions reflect my own implementation and reasoning.
