---
title: Assignment
type: note
domain: C programming
tags:
  - C_Pointer
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---
Pointers can be assigned the address of another variable using the address-of operator `&`.

```C
int num = 10;
int *ptr = &num; // ptr now points to the memory address of num
```