


/// Link Fixes 

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-external-href]').forEach(item => {
        const url = item.getAttribute('data-external-href');
        item.setAttribute('title', url);
        item.style.cursor = 'pointer';
        
        item.addEventListener('click', (e) => {
            // Don't check e.target, just handle any click within the element
            window.open(url, '_blank');
        });
        
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'link');
        item.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                window.open(url, '_blank');
            }
        });
    });

    document.querySelectorAll('[data-internal-href]').forEach(item => {
        const url = item.getAttribute('data-internal-href');
        item.setAttribute('title', url);
        item.addEventListener('click', (e) => {
            window.location.href = url; 
        });

        // Make it keyboard accessible
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'link');

        item.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                item.click();
            }
        });
    });
});

/// Copy Buttons

    
function addCopyButton2(el) { 
    const pre = el.querySelector("pre"); 
    
    const preLangText = pre.getAttribute("data-lang") || "plaintext"; 
    const preCodeText = pre.textContent || pre.innerText; 

    const footer = el.querySelector("code-footer"); 
    const footerLang = el.querySelector("code-footer > code-footer-lang"); 
    const footerCopy = el.querySelector("code-footer > code-footer-copy");
    const footerChars = el.querySelector("code-footer > code-footer-chars"); 

    footerLang.innerText = preLangText; 
    footerChars.innerText = `${preCodeText.length} chars`; 
    footerCopy.innerText = "click to copy";

    footer.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(pre.textContent || pre.innerText);
            
            // Visual feedback
            const originalText = footerCopy.innerHTML;
            footerCopy.innerHTML = "copied...";
            
            // Reset after 2 seconds
            setTimeout(() => {
                footerCopy.innerHTML = originalText;
            }, 1500);
            
        } catch (err) {
            // Fallback for older browsers
            // ...
        }
    });
}
        
// Function to add copy buttons to all pre elements
function addCopyButtons() {
    document.querySelectorAll("code-wrapper").forEach((el, idx) => { 
        addCopyButton2(el); 
    });
}

// Run when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addCopyButtons);
} else {
    addCopyButtons();
}

/// Theme Controls 

    
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
    
/// Christmas Easter Egg 

document.addEventListener('DOMContentLoaded', () => {

    const isChristmas = new Date().getMonth() === 11; // December is month 11 (0-indexed)

    console.log(isChristmas
        ? "christmas detected :)"
        : "christmas not detected :("
    );

    if (isChristmas) { 
        const body = document.querySelector("body")

        const christmasContainer = document.createElement("christmas-container"); 
        body.appendChild(christmasContainer);

        function createSnowflake() {
            const snowflake = document.createElement('christmas-snowflake');

                

            const dur = Math.random() * 3 + 5; 

            snowflake.innerHTML = '❄';
            snowflake.style.left = Math.random() * 100 + '%';
            snowflake.style.animationDuration = dur + 's';
            snowflake.style.fontSize = Math.random() * 3 + 0.5 + 'em';

            christmasContainer.appendChild(snowflake);

            setTimeout(() => {
                snowflake.remove();
            }, dur * 1000);
        }

        // Create initial snowflakes
        for (let i = 0; i < 50; i++) {
            setTimeout(createSnowflake, i * 100);
        }

        // Continuously create new snowflakes
        setInterval(createSnowflake, 200);
    }


    
});