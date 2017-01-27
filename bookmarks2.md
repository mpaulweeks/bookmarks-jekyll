---
layout: page
title: Bookmarks
permalink: /bookmarks2/
---

{% for category in site.data.bookmarks %}
<h1> {{ category.title }} </h1>
{% for link in category.children %}
<p>
<span> {{link.author}} </span>
<a href="{{link.url}}">{{link.title}}</a>
{% for tag in link.tags %}
<span> {{tag}} </span>
{% endfor %}
</p>
{% endfor %}
{% endfor %}
