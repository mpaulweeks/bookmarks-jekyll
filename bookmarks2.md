---
layout: page
title: Bookmarks
permalink: /bookmarks2/
---

{% for category in site.data.bookmarks %}
  <h1> {{ category.section }} </h1>
  {% for link in category.children.links %}
  <p><a href="{{link.url}}">{{link.title}}</a></p>
  {% endfor %}
{% endfor %}
