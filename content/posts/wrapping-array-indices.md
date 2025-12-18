---
title: "Wrapping Indices"
date: 2025-12-18
---

Just in case you needed it, here's a better way to wrap your array indices. 


### The naive approach

The following is the most obvious way to wrap an integer around a specific value. Equivalent to saying, "Increment, but if I would increment passed this value, reset to 0 instead". and, "Decrement, buf if I would decrement below 0, reset to the highest index instead". 

{% code() %} ```c++
int count = 10;
int idx = 0;

// increment
idx = idx == count-1 ? 0 : idx+1;

// decrement
idx = idx == 0 ? count-1 : idx-1;
``` {% end %}

This works well enough, but there is a better solution. 

### The better approach

I fully admit to finding this on [stackoverflow,](https://stackoverflow.com/a/45397704) but it's a clever and concise trick. Here's how it goes. 


{% code() %} ```c++
int count = 10;
int idx = 0;

// increment
++idx;
idx = (idx % count + count) % count;

// decrement
--idx;
idx = (idx % count + count) % count;
``` {% end %}

This approach is more robust (works for increments greater than 1), and doesn't require branching. 
