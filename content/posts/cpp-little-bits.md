---
title: "Little bits of C++"
author: "James Mitchell"
draft: false 
tags: [guide, code, c++]
date: 2025-03-27
updated: 2025-03-27
---


### Get the nth byte of an integer 

```c++

int getByte(int num, unsigned byteno)
{
    // Mask and return the required byte
    return (num >> (byteno * 8)) & 0xFF;    
}

```

### Reserved macro identifiers 
Best practice is to avoid using preceding underscores in macro identifiers. [^1]

```c++
#define foo(x__) x__        // prefer this... 
#define foo(__x__) __x__    // to this (might produce a warning)
``` 

### Misconceptions about `emplace_back` and `push_back`

`emplace_back()` does *not* move the object that is passed to it. [^2]

It simply *forwards* the argument to the constructor of the new object. If it is given an *l-value* then that is what the constructor for the new object will see and the underlying resource will need to be copied. 

The *l-value* must be explicitly converted to an *r-value* with `std::move()` to invoke the correct constructor and avoid a copy. 

Since C++11 `push_back()` has an overload which accepts an *r-value* and thus it can be be used to avoid the copy just the same as `emplace_back()`

```c++
void example() 
{
    auto w = Widget(1,2,3);

    vec.push_back(w);     // creates an unneccessary copy
    vec.emplace_back(w);  // also creates an unneccessary copy

    vec.push_back(std::move(w));    // invokes r-value ctor, no copy
    vec.emplace_back(std::move(w)); // same thing
}
```

### Same name, different compilation unit
Having structs with the _same name_ in separate compilation units can cause undefined behavior. I was getting `std::bad_alloc` exceptions from code that looked like this: 

```c++
// Mesh.cpp
struct vertex_t
{
     GLfloat position[3];
     GLfloat normal[3];
};

// Font3D.cpp
struct vertex_t
{
    GLfloat position[3];
};
```

To the best of my knowledge this shouldn't cause undefined behavior, but regardless I was able to narrow down the problem to being the names of these two structs. 

### A thread-safe singleton for C++11 or newer

A change made to the standard for C++11 makes possible a very simple thread-safe singleton pattern. 

> §6.7 [stmt.dcl] p4
> 
> If control enters the declaration concurrently while the variable is being initialized, the concurrent execution shall wait for completion of the initialization.

```c++
class Singleton
{
public:
    static Singleton& instance()
    {
        static Singleton s;
        return s;
    }
private:
      
};
```

### The Minutia of pointers to union members
Pointers to union members are guaranteed to be equivalent
```c++
union Foo
{
    char    c;
    short   s;
    int     i;
    long    l;
} f;

assert((void*)&f == (void*)&f.c);
assert((void*)&f == (void*)&f.s);
assert((void*)&f == (void*)&f.i);
assert((void*)&f == (void*)&f.l);
```

From _C standard (N1570, 6.7.2.1 Structure and union specifiers)_:
> 16 The size of a union is sufficient to contain the largest of its members. The value of at most one of the members can be stored in a union object at any time. **A pointer to a union object, suitably converted, points to each of its members** (or if a member is a bit- field, then to the unit in which it resides), and vice versa.


### Virtual Destructors (when, why, how)
Needed when you want to delete an object with just a pointer to the base class. [^3]

```c++
class Base
{
    ~virtual Base() {} 
};

class Derived : public Base 
{

};

// ... 

Base* p = new Derived();

// virtual destructor needs to be defined (even an empty one) or else this causes undefined behavior
delete p;
```

### References 

[^1]: [stackoverflow](https://stackoverflow.com/a/22027287)

[^2]: [quuxplusone.github.io](https://quuxplusone.github.io/blog/2021/03/03/push-back-emplace-back/)

[^3]: [stackoverflow](https://stackoverflow.com/a/461224/1103084)