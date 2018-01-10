---
layout: page
title: Bookmarks
permalink: /bookmarks/
---

Articles and videos I am eager to share and preserve.

<a href="/feed/bookmarks.xml"><i class="svg-icon rss"></i></a>

<h3> Tags <a href="?"> (reset) </a></h3>
<div id="tag-holder"></div>

{% assign categories = site.data.bookmarks.categories %}
{% for category in categories %}
<h1 class="block" id="{{category}}"><hr/>{{ category }} </h1>
{% assign links = site.data.bookmarks.links | where: 'category', category %}
{% for link in links %}
<p class="block" data-category="{{category}}">
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

function addTag(tagName){
  var aNode = document.createElement("a");
  aNode.href = '?tags=' + tagName;
  aNode.className = "bookmarks-tag";
  var textnode = document.createTextNode(tagName);
  aNode.appendChild(textnode);
  document.getElementById("tag-holder").appendChild(aNode);
}
var siteData = {{ site.data | jsonify }}.bookmarks;
var allTags = {};
for (var li = 0; li < siteData.links.length; li++){
  var link = siteData.links[li];
  for (var ti = 0; ti < link.tags.length; ti++){
    var tag = link.tags[ti];
    allTags[tag] = true;
  }
}
var sortedTags = Object.keys(allTags).sort();
for (var ti = 0; ti < sortedTags.length; ti++){
  var tag = sortedTags[ti];
  addTag(tag);
}

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
