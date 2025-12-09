---
title: "How I use X-Macros in C++"
author: "James Mitchell"
draft: false
tags: [guide, code, c++]
date: 2025-11-20
updated: 2025-11-25
---

I really like [x-macros](https://en.wikipedia.org/wiki/X_macro), and over the past few years I've been using them more and more in my code. 

Here's an example that demonstrates why they are useful: 

### Example - Enums 

Let's say that I want to enumerate dog breeds. I know which ones I want now, but I'll need to be able to add more later. I'd like to be able to convert the enum value to and from a human-readable string. This is how to do all of that using x-macros.

{% code() %} ```c++
#include <string>
#include <iostream>
using namespace std;

#define EXPAND_ENUM_DOGS(DOG) \
    DOG(DOG_BEAGLE  , "beagle"  ) \
    DOG(DOG_DOBERMAN, "doberman") \
    DOG(DOG_PUG     , "pug"     ) \
    DOG(DOG_POODLE  , "poodle"  ) \
    DOG(DOG_TERRIER , "terrier" ) \
    DOG(DOG_BOXER   , "boxer"   )

#define CASE(_enum, _str) ,_enum
enum Dog { DOG_INVALID EXPAND_ENUM_DOGS(CASE) };
#undef CASE

string to_string(Dog dog)
{
    #define CASE(_enum, _str) case _enum: return _str;
    switch (dog) { EXPAND_ENUM_DOGS(CASE) };
    #undef CASE
    return "DOG_INVALID";
}

Dog to_dog(string const& str)
{
    #define CASE(_enum, _str) if (str == _str) return Dog::_enum;
    EXPAND_ENUM_DOGS(CASE)
    #undef CASE
    return DOG_INVALID;
}

int main()
{
    Dog my_dog = DOG_BEAGLE;

    cout << "My dog is a " << to_string(my_dog) << endl;

    Dog your_dog = DOG_INVALID;

    while (your_dog == DOG_INVALID)
    {
        cout << "What kind of dog do you have? ";
        if (string line; getline(cin, line))
        {
            your_dog = to_dog(line);
            if (your_dog == DOG_INVALID)
                cout << "I've never heard of that before..." << endl;
            else
                cout << "Ah, a '" << to_string(your_dog) << "', how wonderful!" << endl;
        }
    }

    return 0;
}
``` {% end %}

Pay attention to the pre-processor macro `EXPAND_ENUM_DOGS`, that's the important part. It has an input parameter. That parameter is itself ANOTHER pre-processor macro with its own input parameters. 

It doesn't define anything on it's own, but can be used by its input (`DOG`, in this example) to do something useful. This is a form of [Metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming). Your pre-defined data elements are encoded within the macro, which becomes the source of truth any code you may want to generate. 

To demonstrate, look closely at the `to_string` function:

{% code() %} ```c++
string to_string(Dog dog)
{
    #define CASE(_enum, _str) case _enum: return _str;
    switch (dog) { EXPAND_ENUM_DOGS(CASE) }; // <--- Pay attention to this line
    #undef CASE
    return "DOG_INVALID";
}
``` {% end %}

This is the literal expansion of `EXPAND_ENUM_DOGS(CASE)`

{% code() %} ```c++
case DOG_BEAGLE: return "beagle";
case DOG_DOBERMAN: return "doberman";
case DOG_PUG: return "pug";
case DOG_POODLE: return "poodle";
case DOG_TERRIER: return "terrier";
case DOG_BOXER: return "boxer";
``` {% end %}

And again, look at the `to_dog` function

{% code() %} ```c++
Dog to_dog(string const& str)
{
    #define CASE(_enum, _str) if (str == _str) return Dog::_enum;
    EXPAND_ENUM_DOGS(CASE) // <--- Pay attention to this line
    #undef CASE
    return DOG_INVALID;
}
``` {% end %}

The same macro `EXPAND_ENUM_DOGS(CASE)` expands differently, since it sees a new definition for `CASE`

{% code() %} ```c++
if (str == "beagle") return Dog::DOG_BEAGLE;
if (str == "doberman") return Dog::DOG_DOBERMAN;
if (str == "pug") return Dog::DOG_PUG;
if (str == "poodle") return Dog::DOG_POODLE;
if (str == "terrier") return Dog::DOG_TERRIER;
if (str == "boxer") return Dog::DOG_BOXER;
``` {% end %}

The key idea is to repeat against the execution of a pre-processor macro. This ability can then be leveraged to eliminate large repeating patterns in your code, as well as guarantee correctness. 

Ever since I learned this technique, I have used it extensively in my own code. It makes working with enums in C++ much more functional than the base language allows. I have also used it to implement a light-weight form of polymorphism. The performance benefits are also pretty clear, this dog breed example could have been written with a lookup table, which would have incurred an additional memory and runtime cost.  

If you want more practical examples of this trick, see my code library [ut](https://github.com/jmitchell24/ut), which I actively maintain on github and uses x-macros throughout (hint: look specifically at [color.hpp](https://github.com/jmitchell24/ut/blob/master/include/ut/color.hpp).