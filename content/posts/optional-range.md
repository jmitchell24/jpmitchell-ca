---
title: "Range support in std::optional<T>, and why that isn't ridiculous."
author: "James Mitchell"
draft: false
tags: [c++]
date: 2025-10-23
updated: 2025-10-23
---



For C++26, a proposal has been made to add range support to std::optional. That means code that looks like this will become valid C++. 

```c++

std::optional<int> foo = 722; 

for (int i : foo) 
{
    std::cout << "This Actually Prints? " << ( i ) << std::endl;
}

```

At first blush this seems strange, but it can make a lot of sense, given the right perspective on what std::optional actually is. 

One (quite intuitive) way to look at std::optional is to see it as a nullable type, or even just a pointer with a layer of memory safety. Equivalent to this c-style code. 

```c

int val = 722;

int* optional_val = NULL; 

if (optional_val != NULL)
{
    std::cout << "This will not print: " << ( *optional_val ) << std::endl;
}

optional_val = &val; 

if (optional_val != NULL)
{
    std::cout << "This will print: " ( *optional_val ) << std::endl; 
}

```

But another way to conceptualize std::optional is as a range. For myself this definition helps make sense of the idea: 

> A range of values that has only 0 or 1 elements.

This framing is not without precident, this conception of optional values exists already in other languages such as Rust (among many others). 

```rust 

let foo: Option<i32> = Some(722);
    
for i in foo {
    println!("This Actually Prints? {}", i);
}

```

I personally like this framing. I also like the improved 'elegance' of syntax for what is ultimately an extremely common code pattern. 

For more information, you can see the proposal [here](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3168r1.html). 