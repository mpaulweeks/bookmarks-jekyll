---
layout: panel
title: Diagnosing Your Anime Taste
convention: Anime Central 2017
isPanel: true
permalink: /acen-2017/diagnosing-taste/
---

{% assign data = site.data.conventions.acen-2017.diagnosing-taste %}

<div class="manga-header"> References </div>
{% for link in data.references %}
  <li class="manga-link">
    {% if link.url %}
      <a href="{{link.url}}" target="_blank">{{link.title}}</a>
    {% else %}
      <span>{{link.title}}</span>
    {% endif %}
  </li>
{% endfor %}
