---
title: "What happens when you click on my face?"
author: "James Mitchell"
draft: true 
tags: []
date: 2025-06-03
updated: 2025-06-03
---

Have you ever tried clicking on my face? Hopefully something like this happens: 

<video width="640" height="360" controls>
  <source src="/img/easter-egg.mp4" type="video/mp4">
  
  Your browser doesn't support video playback.
</video>

When you click on my face, a little animation appears. I made it using [Zdog](https://zzz.dog/). 

<script src="https://unpkg.com/zdog@1/dist/zdog.dist.min.js"></script>

{% zdog(id="zdog-canvas-test1") %}

// add circle
new Zdog.Ellipse({
  addTo: illo,
  diameter: 80,
  stroke: 20,
  color: '#636',
});

{% end %}

{% zdog(id="zdog-canvas-test2") %}

// add circle
new Zdog.Ellipse({
  addTo: illo,
  diameter: 80,
  stroke: 20,
  color: '#fff',
});

{% end %}