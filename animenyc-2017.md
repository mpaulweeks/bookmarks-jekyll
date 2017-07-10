---
layout: page
title: Anime NYC 2017
permalink: /animenyc-2017/
---

Coming soon...

{% assign all_panels = site.posts | where: "type", "panel" %}
{% assign panels = all_panels | where: "convention", "Anime NYC 2017" %}
{% include panels.html panels=panels %}
