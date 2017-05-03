---
layout: panel
title: Diagnosing Your Anime Taste
convention: Anime Central 2017
isPanel: true
permalink: /acen-2017/diagnosing-taste/
---

{% assign data = site.data.conventions.acen-2017.diagnosing-taste %}

<div class="manga-header"> References </div>
{% for link in data.articles %}
  <li class="manga-link">
    {% if link.url %}
      <a href="{{link.url}}" target="_blank">{{link.title}}</a>
    {% else %}
      <span>{{link.title}}</span>
    {% endif %}
  </li>
{% endfor %}
{% for link in data.videos %}
  <div class="video-embed">
    <iframe width="560" height="315" src="{{link.url}}" frameborder="0" allowfullscreen></iframe>
  </div>
{% endfor %}
