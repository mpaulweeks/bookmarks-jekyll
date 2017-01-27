---
layout: page
title: Bookmarks
permalink: /bookmarks2/
---

{% for category in site.data.bookmarks %}
<h1> {{ category.title }} </h1>
{% for link in category.children %}
<p>
{% if link.author.size > 0 %}
<span class="bookmarks-author"> {{link.author}} </span><br/>
{% endif %}
<a href="{{link.url}}">{{link.title}}</a>
{% if link.tags.size > 0 %}
<br/>
{% for tag in link.tags %}
<span class="bookmarks-tag"> {{tag}} </span>
{% endfor %}
{% endif %}
</p>
{% endfor %}
{% endfor %}
