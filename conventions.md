---
layout: page
title: Conventions
permalink: /conventions/
---

<p>
  Linked below are convention panels I've presented, with citations and further readings.
</p>

{% assign all_panels = site.posts | where: "type", "panel" %}
{% assign panels = all_panels | where: "isLive", "true" %}
{% include panels.html panels=panels %}
