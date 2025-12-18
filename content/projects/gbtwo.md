---
title: GBTWO 
date: 2025-08-09
updated: 2025-12-18
extra: 
    type: "Hardware Emulator"
    platforms: [ "Web", "Linux", "Windows" ]
    summary: "An emulator and hardware showcase of the original Nintendo handheld."
    screenshots: [ "/img/project-gbtwo.png" ]
---

### Overview

GBTWO is my Gameboy emulator. It's accurate enough to play many commercial and homebrew games. The goal of the project was to learn the hardware of the Gameboy, moresoe than to play the games themselves. For that purpose existing emulators such as [Gambatte](https://emulation.gametechwiki.com/index.php/Gambatte) are a much better choice. 

### Features

- **Compatible**: Plays many commercial and homebrew games. 
- **Multi Platform**: The build system for this project targets Linux, Windows, and Web (via WASM/Emscripten, see below).
- **A Hardware Showcase**: Comprehensive GUI for viewing and interacting with the emulator while games are running. 

### Development

GBTWO is a project that I began in August 2025. I had attempted many years ago to create a Gameboy emulator, but I was ultimately unsuccessful. Life circumstances provided me with the time to make a second attempt (explains the name). I consider this project wildly more successful, even in its current state. I plan to continue development for the foreseeable future, and to maintain the WASM/Emscripten build for posterity here, on my personal site.

I have no intention to release the source code, but I will always keep the web build freely available on this page. 

### Screenshots

{{ screenshot_list(cols=1, cols_mobile=1) }}

{% big_link(url="/apps/gbtwo.html", icon="play") %} 
Launch GBTWO 
{% end %}