---
title: Null pointer
type: note
domain: C programming
tags:
  - C_Pointer
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

Pointers can be assigned a special value `NULL` to indicate that they are not pointing to any valid memory location.

```c
int *ptr = NULL; // ptr is a NULL pointer
```


The purpose of NULL pointer:

- **Initialization**: When you declare a pointer variable but don't have a specific memory location to assign to it immediately, you can initialize it to `NULL` to signify that it's not pointing to anywhere yet.
- **Error handling**: `NULL pointers` are often used to indicate errors or exceptional conditions, such as when a function fails to allocate memory or when a search operation fails to find a desired element. Function may be return `NULL` to signal that an operation was unsuccessful.
- **Terminal condition**: In linked data structures like linked list, tree, or graphs, `NULL` pointers are commonly used to indicate the end of a chain or a leaf node. This help in traversing and iterating through these data structures.
- **Avoiding dangling pointers**: Setting a pointer to `NULL` after freezing the memory it point to helps avoid dangling pointers. A dangling pointer that continues to point to a memory location after its content has been deal-located. 
- **Conditional checking**: Before de-referencing a pointer, it's common practice to check if it's `NULL` to avoid accessing invalid memory locations, which could lead to program crashes or undefined behavior.


