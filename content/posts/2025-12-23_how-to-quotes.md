---
title: How I made a Quote of the Day 
date: 2025-12-23
--- 

Here's how I made a 'Quote of the Day' for one of my websites. It's very simple and you should be able to add it to your site just as quickly as I did. 

### First the HTML & CSS... 

{% code() %} ```html
<region>
    <region-title>
        Quote of the Day
    </region-title>

    <region-content>
        <daily-quote></daily-quote>
    </region-content>
</region>
``` {% end %}

{% code() %} ```css
daily-quote { 
    color: var(--color-gray); 
    padding: var(--space-2); 
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
    border: var(--border-size) dashed var(--color-dark);
    border-radius: var(--border-radius);
}
``` {% end %}

I prefer using custom html tags, but this still works perfectly if you use either id's or classes. 

### Then just a bit of Javascript... 

{% code() %} ```javascript
const quoteArray = [ 
    { author: "Charlie Brown", text: "In the book of life, the answers aren't in the back." },
    // ... 
];

const today = new Date();
const dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / 86400000);
const seed = dayOfYear * 9301 + 49297;
const randomIndex = seed % quoteArray.length;
const randomQuote = quoteArray[randomIndex];
const quote = document.querySelector("daily-quote"); 
quote.innerHTML = `${randomQuote.text} <br><br> - ${randomQuote.author}`;
``` {% end %}

The goal is to always pick the same quote for any given day. I create a random-feeling but deterministic shuffle using the `seed` value just to break up the sequence, to reduce repeating patterns in the quotes. 

### And then write your blog post about it...

That's all there is to it, very simple. I figure it took me about half an hour to whip together. This is a nice little feature to have. If you ever find an insightful, interesting, or funny quote that you like you can have a place to share it with others. 


