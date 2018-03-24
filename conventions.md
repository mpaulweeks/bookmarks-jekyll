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
{% assign conventions = panels | map: 'convention' | uniq %}

{% for con in conventions %}
  {% assign cpanels = panels | where: 'convention', con %}
  <h1> {{ con }} </h1>
  {% include convention.html convention=con %}
{% endfor %}
