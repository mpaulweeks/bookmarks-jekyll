---
layout: panel
title: Diagnosing Your Anime Taste
convention: Anime Central 2017
type: panel
permalink: /acen-2017/diagnosing-taste/
---

{% assign data = site.data.conventions.acen-2017.diagnosing-taste %}

<div class="manga-header"> Articles </div>
{% for link in data.articles %}
  <li class="manga-link">
    {% if link.url %}
      <a href="{{link.url}}" target="_blank">{{link.title}}</a>
    {% else %}
      <span>{{link.title}}</span>
    {% endif %}
  </li>
{% endfor %}
<div class="manga-header"> Videos </div>
{% for link in data.videos %}
  <li class="manga-link">
    <a href="https://youtu.be/{{link.youtube}}" target="_blank">{{link.title}}</a>
  </li>
{% endfor %}
