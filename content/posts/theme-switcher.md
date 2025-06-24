---
title: "How I made this site's theme switcher"
author: "James Mitchell"
draft: false 
tags: []
date: 2025-06-24
updated: 2025-06-24
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

Full disclosure, I used Anthropic's [Claude](https://claude.ai) 🤖 to help decide the color names.  

### CSS 

Nothing particularily interesting here.

The relevant detail is just that the theme color is being displayed prominantly on the button (through the `:hover` and `.theme-active` selector). 

```css
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

First decide the inital theme to set. Either a previously selected theme, or a default value.

The `setTheme` function does the following: 
- Sets the correct `data-theme` attribute for the `body` element. This is what applies the theme to the entire page. 
- Update all the `theme-switcher-button` elements. Add or remove the `theme-active` tag to reflect the currently selected theme.
- Save selection to `localStorage`, and the `current_theme` variable. 

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

