---
title:  Markdown Test Page
date: 2025-05-26
updated: 2025-05-26
draft: true 
---

### Headings

# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading

### Links

[Link text](/)

[Link with title](/blog 'My blog!')

### Images

![Markdown logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
![Syki Logo](/logo512.png 'My logo')

### Lists

#### Unordered

-   Lorem ipsum dolor sit amet
-   Lorem ipsum dolor sit amet
    -   Lorem ipsum dolor sit amet
        -   Lorem ipsum dolor sit amet
        -   Lorem ipsum dolor sit amet
        -   Lorem ipsum dolor sit amet
-   Lorem ipsum dolor sit amet

#### Ordered

1. Lorem ipsum dolor sit amet
2. Lorem ipsum dolor sit amet
3. Lorem ipsum dolor sit amet

Start numbering with offset:

57. Lorem ipsum dolor sit amet
1. Lorem ipsum dolor sit amet

#### Checkboxes

-   [ ] Lorem ipsum dolor sit amet
-   [x] Lorem ipsum dolor sit amet
-   [ ] Lorem ipsum dolor sit amet

### Emphasis

**Bold text**

_Italic text_

~~Strikethrough~~

### Horizontal Rule

---

### Blockquotes

> Blockquotes
>
> > Nested blockquotes
> >
> > > Nested blockquotes

### Code

Inline `code`

```
Sample text here...
```

Syntax highlighting

```js
var foo = function (bar) {
    return bar++
}

console.log(foo(5))
```

### Tables

{% table() %}
| Heading1 | Heading2                   |
| -------- | -------------------------- |
| row1     | Lorem ipsum dolor sit amet |
| row2     | Lorem ipsum dolor sit amet |
| row3     | Lorem ipsum dolor sit amet |
{% end %}

Right aligned columns

{% table() %}
| Heading1 |                   Heading2 |
| -------: | -------------------------: |
|     row1 | Lorem ipsum dolor sit amet |
|     row2 | Lorem ipsum dolor sit amet |
|     row3 | Lorem ipsum dolor sit amet |
{% end %}

### HTML

This is inline <span style="color: red;">html</span>

<audio controls>
    <source src="/uploads/medium-drill-burst.mp3" type="audio`/mpeg" />
    Your browser does not support the audio element.
</audio>

### XSS Atack

<!-- <script>alert('XSS Atack. When you see this you should use sanitizer.')</script> -->

### Lots of text 

It began with the forging of the Great Rings. Three were given to the Elves; immortal, wisest and fairest of all beings. Seven to the Dwarf Lords, great miners and craftsmen of the mountain halls. And nine...Nine rings were gifted to the Race of Men, who above all else desire power. For within these rings was bound the strength and will to govern each race. But they were all of them deceived, for another ring was made. In the land of Mordor, in the fires of Mount Doom, the Dark Lord Sauron forged, in secret, a Master Ring to control all others. And into this Ring he poured all his cruelty, his malice and his will to dominate all life. One Ring to rule them all.


### More code 

the `quick` brown `fox` jumps `over` the `lazy` dog.

```c++

#include <iostream>
using namespace std;
int main() {
    cout << "Hello World!" << endl;
    return 0;
}

```