---
title: "How I made this site's theme switcher"
author: "James Mitchell"
draft: false 
tags: []
date: 2025-06-24
updated: 2025-11-25
---

I just finished adding a theme switcher to my site. 
It's now available on the [Extra](/extra) page. 
This was fairly straight-forward, and I managed to complete it start-to-finish in an hour or two. 
For the sake of posterity, and to help anyone who might stumble 👢 onto this page, 
here's how I did it. 

### HTML

This is the html for the theme selector. I prefer to use custom tags instead of ids or classes. 
`onclick` is set to call the js function that will perform the switch. 
`data-theme` declares the theme assigned to the button. 

```html
<theme-switcher> 
    <theme-switcher-button onclick="setTheme('alt0')" data-theme="alt0"> Coral Burst </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt1')" data-theme="alt1"> Sunset Pink </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt2')" data-theme="alt2"> Violet Bloom </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt3')" data-theme="alt3"> Lavender Light </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt4')" data-theme="alt4"> Sky Blue </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt5')" data-theme="alt5"> Ocean Breeze </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt6')" data-theme="alt6"> Mint Fresh </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt7')" data-theme="alt7"> Spring Green </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt8')" data-theme="alt8"> Lime Zest </theme-switcher-button>  
    <theme-switcher-button onclick="setTheme('alt9')" data-theme="alt9"> Golden Honey </theme-switcher-button>  
</theme-switcher>
```

### CSS 

Nothing particularily interesting here.
All accents across the site use the `--color-primary` variable. I created a separate selector for all potential values of the `data-theme` attribute. 
The relevant detail is just that the theme color is being displayed prominantly on the button (through the `:hover` and `.theme-active` selector). 

```css

:root {
    --color-primary: #fac863;

    --color-darker: #2b2c2f;
    --color-dark: #38393c;
    --color-gray: #88898d;
    --color-light: #e7e8ed;
    --color-lighter: #feffff;
}

[data-theme="alt0"] { --color-primary: #fa6363; }
[data-theme="alt1"] { --color-primary: #fa63a8; }
[data-theme="alt2"] { --color-primary: #c863fa; }
[data-theme="alt3"] { --color-primary: #8363fa; }
[data-theme="alt4"] { --color-primary: #63a8fa; }
[data-theme="alt5"] { --color-primary: #63fac8; }
[data-theme="alt6"] { --color-primary: #63fa83; }
[data-theme="alt7"] { --color-primary: #83fa63; }
[data-theme="alt8"] { --color-primary: #c8fa63; }
[data-theme="alt9"] { --color-primary: #fac863; }

theme-switcher { 
    display: flex;
    flex-direction: column;
    width: fit-content;
    gap: var(--space-2);
}

theme-switcher-button { 
    background-color: var(--color-dark);
    color: var(--color-light);
    font-size: var(--text-h4);
    text-decoration: none;
    border-radius: .5rem;
    border: 0;
    border-left: var(--space-3) solid var(--color-primary); 
    padding: var(--space-2);
    width: auto;
    display: flex;
    gap: var(--space-2);
    align-items: center;
    cursor: pointer;
}

theme-switcher-button:hover, 
theme-switcher-button.theme-active {
    background-color: var(--color-primary);
    color: var(--color-darker);
    border-radius: .5rem;
}

@media (max-width: 768px) {
    theme-switcher { 
        width: auto;
    }
}
```

### Javascript

This is the important part. 
First, I get the inital value for the selected theme. I pull a previously selected theme from `localStorage` if it exists, otherwise I set a default. 

```javascript 
const THEME_KEY = "selected-theme"; 
let current_theme = localStorage.getItem(THEME_KEY) || "alt9"; 
```

Next I setup a function to perform the switch. 

```javascript
function setTheme(theme) { 
    document.body.setAttribute("data-theme", theme); 
    document.querySelectorAll("theme-switcher-button").forEach(btn => { 
        const btn_theme = btn.getAttribute("data-theme"); 
        if (btn_theme == theme) 
            btn.classList.add("theme-active"); 
        else 
            btn.classList.remove("theme-active"); 
    });

    localStorage.setItem(THEME_KEY, theme); 
    current_theme = theme; 
}
```

It does the following: 
- Set the `data-theme` attribute on the `body` element. This is what applies the new color to the entire page. 
- Find all theme switcher buttons on the page (if any)
- Set the state of the buttons based on the selected theme. 
- Save the newly selected theme to `localStorage`
- Set a variable `current_theme` for future reference while the the page is loaded in the browser. 

Here's the complete code (feel free to copy/paste 😉)  

```javascript
const THEME_KEY = "selected-theme"; 
let current_theme = localStorage.getItem(THEME_KEY) || "alt9"; 
    
function setTheme(theme) { 
    document.body.setAttribute("data-theme", theme); 

    document.querySelectorAll("theme-switcher-button").forEach(btn => { 
        const btn_theme = btn.getAttribute("data-theme"); 
        if (btn_theme == theme) 
            btn.classList.add("theme-active"); 
        else 
            btn.classList.remove("theme-active"); 
    });

    localStorage.setItem(THEME_KEY, theme); 
    current_theme = theme; 
}

setTheme(current_theme);

```

And that is all there is to it! 