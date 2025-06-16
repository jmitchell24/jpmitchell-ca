---
title: "Feeling like a wizard on my Desktop (keyd guide)"
author: "James Mitchell"
draft: true 
tags: []
date: 2025-06-06
updated: 2025-06-06
---

I really like [keyd](https://github.com/rvaiya/keyd). It's a key remapping program for linux that is easy to to setup and very powerful. 

The effect it has had on how I interface with my PC has been profound. It has enabled me to build a system of macros that enables me to navigate through my apps at a pace that I've never been able to before. 

Here I'll explain how I use keyd, but my reccomendation to you is to learn how the configuration works, then start experimenting, and create a system of macros that best suits your needs and preferences. 

### How to get and install Keyd 

Keyd is hosted on github, and can be installed to your local machine using a few simple commands. 

```bash 
git clone https://github.com/rvaiya/keyd
cd keyd
make && sudo make install
sudo systemctl enable --now keyd
```

To get started, you will need to create a configuration file at `/etc/keyd/default.conf`.


This is my entire configuration file, I'll break down and explain each section in detail: 

> TODO a link to the entire script 

```
[ids] 
*

[main]
capslock    = overload(nav, esc)

# Razer MACROS (top down): f13, f14, f15, f16, f17
f15 = A-left
f16 = A-right


[nav]
;       = capslock
j       = left
i       = up
k       = down
l       = right
u       = home
o       = end
.       = delete
/       = backspace
m       = pageup
,       = pagedown
q       = A-f4
a       = leftshift 
w       = C-S-A-w
e       = C-S-A-e
r       = C-S-A-r
p       = C-S-A-p


up      = C-S-A-up
down    = C-S-A-down
left    = C-S-A-left
right   = C-S-A-right
```


### Caps lock function layer 

These lines remap capslock to a toggle for the macro layer. This is the only change that gets made to the default key mappings, all macros are only enabled when capslock is held. If you are wondering how capslock gets toggled if the key is remapped, don't worry this is accounted for, as I will explain further along. 

```
[ids] 
*

[main]
capslock    = overload(nav, esc)
```


### my (beloved) razer keyboard macros 

This section is for remapping the macro keys on my personal keyboard, the Razer BlackWidow 2013. 

```
# Razer MACROS (top down): f13, f14, f15, f16, f17
f15 = A-left
f16 = A-right
```

### my right hand 

This section defines the macros for the keys that I can access with my right hand. 


<kbd>i</kbd>  
jkl

```
j       = left
i       = up
k       = down
l       = right
u       = home
o       = end
.       = delete
/       = backspace
m       = pageup
,       = pagedown

```

### my left hand 

```
q       = A-f4
a       = leftshift 
```