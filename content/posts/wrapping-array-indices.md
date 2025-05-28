---
title: "Wrapping Array Indices"
tags: [guide, code]
date: 2025-03-26
updated: 2025-03-26
draft: true 
---

# Wrapping Array Indices (a better approach)

## Objective

Keep an array index value within the correct range while incrementing and decrementing. 

## (My) naive approach

```c++

int count = 10;
int idx = 0;

// increment
idx = idx == count-1 ? 0 : idx+1;

// decrement
idx = idx == 0 ? count-1 : idx-1;

```

This works well enough, but there is a better solution. 

## Better approach

Use modulo[^1]

```c++

int count = 10;
int idx = 0;

// increment
++idx;
idx = (idx % count + count) % count;

// decrement
--idx;
idx = (idx % count + count) % count;

```

This approach is more robust (works for increments greater than 1), and doesn't require branching. 

[^1]: https://stackoverflow.com/a/45397704