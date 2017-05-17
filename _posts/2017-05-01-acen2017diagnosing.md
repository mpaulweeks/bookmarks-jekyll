---
layout: panel
title: How to Diagnose Your Anime Taste
convention: Anime Central 2017
type: panel
permalink: /acen-2017/diagnosing-taste/
---

{% assign data = site.data.conventions.acen-2017.diagnosing-taste %}

<div class="panel-description">
<br/>
  Have you ever started a show based on the promising premise/studio/director, only to be disappointed? Then you probably just weren’t looking at the right things! Come to this panel, where we explore why we like what we like. Together, we will gain a new awareness of how art affects us.
</div>

<div class="manga-header"> Articles </div>
{% for link in data.articles %}
  <div class="manga-link">
    {{link.author}} -
    {% if link.url %}
      <a href="{{link.url}}" target="_blank">{{link.title}}</a>
    {% else %}
      <span>{{link.title}}</span>
    {% endif %}
  </div>
{% endfor %}
<div class="manga-header"> Videos </div>
{% for link in data.videos %}
  <div class="manga-link">
    {{link.author}} -
    {% if link.youtube %}
      <a href="https://youtu.be/{{link.youtube}}" target="_blank">{{link.title}}</a>
    {% else %}
      <a href="{{link.url}}" target="_blank">{{link.title}}</a>
    {% endif %}
  </div>
{% endfor %}
