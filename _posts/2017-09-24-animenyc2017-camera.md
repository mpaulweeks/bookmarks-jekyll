---
layout: panel
title: The Simulated Camera
convention: Anime NYC 2017
type: panel
isLive: false
permalink: /animenyc-2017/simulated-camera/
descrip: Resources for a panel hosted at Anime NYC 2017
---

{% assign data = site.data.conventions.animenyc-2017.simulated-camera %}

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

<div class="manga-header">Resources</div>
{% include links.html links=data.resources %}

<div class="manga-header"> Articles </div>
{% include links.html links=data.articles %}

<div class="manga-header"> Videos </div>
{% include links.html links=data.videos %}
