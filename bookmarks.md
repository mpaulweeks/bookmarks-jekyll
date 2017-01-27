---
layout: page
title: Bookmarks
permalink: /bookmarks/
---

<a href="?" id="bookmarks-back" class="bookmarks-back hide">go back to full list</a>

{% for category in site.data.bookmarks %}
<h1 class="block" id="{{category.title}}"> {{ category.title }} </h1>
{% for link in category.children %}
<p class="block" data-category="{{category.title}}">
{% if link.author.size > 0 %}
<a href="?author={{link.author}}" class="hover bookmarks-author" data-author="{{link.author}}"> {{link.author}} </a><br/>
{% endif %}
<a href="{{link.url}}" class="hover">{{link.title}}</a>
{% if link.tags.size > 0 %}
<br/>
{% for tag in link.tags %}
<a href="?tags={{tag}}" class="bookmarks-tag" data-tag="{{tag}}"> {{tag}} </a>
{% endfor %}
{% endif %}
</p>
{% endfor %}
{% endfor %}

<script>
var read_url_param = function(param_name, as_list){
  as_list = as_list || false;
  var vars = {};
  var q = document.URL.split('?')[1];
  if(q != undefined){
    q = q.split('&');
    for(var i = 0; i < q.length; i++){
      var param = q[i].split('=');
      var name = param[0];
      var value = param[1];
      vars[name] = vars[name] || [];
      vars[name].push(value);
    }
  }
  if (vars.hasOwnProperty(param_name)){
    if (vars[param_name].length == 1 && !as_list){
      return vars[param_name][0];
    }
    return vars[param_name];
  }
  return null;
};

var hideElement = function(element){
  element.className += " hide";
}

var showElement = function(element){
  element.className += " show";
}

var filterBookmarks = function(filterTags, tagClass, tagData){
  for (var ft = 0; ft < filterTags.length; ft++){
    var filterTag = filterTags[ft];
    var tags = document.getElementsByClassName(tagClass);
    for (var i = 0; i < tags.length; i++) {
      var tag = tags[i];
      if (tag.getAttribute(tagData) == filterTag){
        showElement(tag.parentElement);
        var category = tag.parentElement.getAttribute("data-category");
        var header = document.getElementById(category);
        showElement(header);
      }
    }
  }
  var toHide = document.querySelectorAll(".block:not(.show)");
  for (var i = 0; i < toHide.length; i++){
    var block = toHide[i];
    hideElement(block);
  }
  var backLink = document.getElementById("bookmarks-back");
  backLink.className = backLink.className.replace(/\bhide\b/,'');
}

var filter = read_url_param("tags", true);
if (filter){
  filterBookmarks(filter, 'bookmarks-tag', 'data-tag');
} else {
  var author = read_url_param("author");
  if (author){
    author = author.split("%20").join(" ");
    filterBookmarks([author], 'bookmarks-author', 'data-author');
  }
}
</script>
