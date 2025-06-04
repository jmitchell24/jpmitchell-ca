---
title: "What happens when you click on my face"
author: "James Mitchell"
draft: true 
tags: []
date: 2025-06-03
updated: 2025-06-03
---

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