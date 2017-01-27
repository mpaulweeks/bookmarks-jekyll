---
layout: page
title: Bookmarks
permalink: /bookmarks2/
---

{% for category in site.data.bookmarks %}
<h1 class="block"> {{ category.title }} </h1>
{% for link in category.children %}
<p class="block" data-category="{{category.title}}">
{% if link.author.size > 0 %}
<span class="bookmarks-author"> {{link.author}} </span><br/>
{% endif %}
<a href="{{link.url}}">{{link.title}}</a>
{% if link.tags.size > 0 %}
<br/>
{% for tag in link.tags %}
<a href="blank" class="bookmarks-tag" data-tag="{{tag}}"> {{tag}} </a>
{% endfor %}
{% endif %}
</p>
{% endfor %}
{% endfor %}

<script>
function filterByTag(filter){
  var tags = document.getElementsByClassName('bookmarks-tag');
  for (var i = 0; i < tags.length; i++) {
    var tag = tags[i];
    if (tag.getAttribute("data-tag") == filter){
      tag.parentElement.className += " show";
      // tag.parentElement.parentElement.className += " show";
    }
  }
  console.log(tags.length);
  var toHide = document.querySelectorAll(".block:not(.show)");
  for (var i = 0; i < toHide.length; i++){
    var tag = toHide[i];
    tag.className += " hide";
  }
  console.log(toHide.length);
}

var filter = "Ping Pong"; // get url-param
if (filter){
  filterByTag(filter);
}
</script>
