---
layout: page
title: Anime NYC 2017
permalink: /animenyc-2017/
---

<p>
  Coming soon...
</p>

{% assign panels = site.posts | where: "type", "panel" %}
{% assign panels = panels | where: "convention", "Anime NYC 2017" %}
{% assign panels = panels | where: "isLive", "true" %}
{% include panels.html panels=panels %}
