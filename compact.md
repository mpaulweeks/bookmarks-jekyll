---
layout: page
title: Compact Bookmarks
permalink: /compact/
---

{% assign links = site.data.bookmarks.links | sort: 'added' | reverse %}
{% for link in links %}
<p>
{{link.added}} <a href="{{link.url}}" class="hover">{{link.title}}</a>
</p>
{% endfor %}
