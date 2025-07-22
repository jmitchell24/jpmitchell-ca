---
title: "Why I love keyd"
author: "James Mitchell"
draft: true
tags: []
date: 2025-07-13
updated: 2025-07-13
---

[keyd](https://github.com/rvaiya/keyd) is amazing. 

Here's why. 

If you (like me) spend most of your day on a linux desktop, then you navigate through your apps with a combination of your keyboard and mouse. You're probably pretty nimble, your mousing is precise and you've memorized a bunch of common keyboard shortcuts. You have the skill you need get the job done. 

But what if you could go faster? Navigate large documents without taking your hands off the home row? Kill, launch or move your apps using only your keyboard. You can do this with keyd, and so much more. 

Here I'll explain how I use keyd, but I strongly recommend that you learn the configuration syntax, then start experimenting, and create a system of macros and shortucts that best suits your needs and preferences. 

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