---
layout: default
title: Conventions
permalink: /conventions/
---

<h1 class="center">
  Conventions
</h1>

<p>
  Linked below are convention panels I've presented, with citations and further readings.
</p>

{% assign panels = site.posts | where: "type", "panel" %}
{% assign panels = panels | where: "isLive", "true" %}
{% include panels.html panels=panels convention=true location=false %}
