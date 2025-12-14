---
title: Pointer Arithmetic
type: note
domain: C programming
tags:
  - C_Pointer
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

Pointers can be ***incremented*** or ***decremented***, and arithmetic operations can be performed on them. This is especially useful when dealing with arrays.  

```C
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr; // ptr points to the first element of the array

printf("%d\n", *ptr); // prints the value at the first element (1)
ptr++; // moves the pointer to the next element
printf("%d\n", *ptr); // prints the value at the second element (2)
```