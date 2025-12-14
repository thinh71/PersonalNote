---
title: Sorting Algorithms
type: note
domain: Algorithms
tags:
  - sorting
  - draft
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---
| Algorithm      | Average Time Complexity | Worst-case Time Complexity | Best-case Time Complexity | Space Complexity | Stability | Suitable For                         | Remarks                                               |
| -------------- | ----------------------- | -------------------------- | ------------------------- | ---------------- | --------- | ------------------------------------ | ----------------------------------------------------- |
| Bubble Sort    | O(n^2)                  | O(n^2)                     | O(n)                      | O(1)             | Stable    | Small datasets, nearly sorted arrays | Simple implementation, inefficient for large datasets |
| Insertion Sort | O(n^2)                  | O(n^2)                     | O(n)                      | O(1)             | Stable    | Small datasets, nearly sorted arrays | Efficient for small datasets and nearly sorted arrays |
| Selection Sort | O(n^2)                  | O(n^2)                     | O(n^2)                    | O(1)             | Unstable  | Small datasets, nearly sorted arrays | Simple implementation, inefficient for large datasets |
| Merge Sort     | O(n log n)              | O(n log n)                 | O(n log n)                | O(n)             | Stable    | Large datasets, linked lists         | Efficient, but requires extra space for merging       |
| Quick Sort     | O(n log n)              | O(n^2)                     | O(n log n)                | O(log n)         | Unstable  | Large datasets, arrays               | Efficient, but worst-case scenario can be slow        |
| Heap Sort      | O(n log n)              | O(n log n)                 | O(n log n)                | O(1)             | Unstable  | Large datasets, arrays               | Efficient, but not a stable sorting algorithm         |
