---
layout: page
title: Conventions
permalink: /conventions/
---

{% assign all_panels = site.posts | where: "type", "panel" %}
{% assign panels = all_panels | where: "isLive", "true" %}
{% include panels.html panels=panels %}
