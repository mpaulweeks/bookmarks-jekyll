---
layout: page
title: Conventions
permalink: /conventions/
---

<div class="posts">
  {% for post in site.posts %}
    {% if post.isPanel %}
    {% unless post.isHidden %}
      <div class="convention-post">

        <a href="{{ site.baseurl }}{{ post.url }}">
          <div class="convention-list-title">{{ post.title }}</div>
        </a>
        <div class="convention-list-subtitle">{{ post.convention }}</div>

      </div>
    {% endunless %}
    {% endif %}
  {% endfor %}
</div>
