---
layout: page
title: Conventions
permalink: /conventions/
---

<p>
  Linked below are convention panels I've presented, with citations and further readings.
</p>

{% assign panels = site.posts | where: "type", "panel" %}
{% assign panels = panels | where: "isLive", "true" %}
{% include panels.html panels=panels convention=true location=false %}
